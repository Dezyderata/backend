import os
import re
import json
import calendar
import sys
import requests
from datetime import datetime
from base import engine, Base
from model import (person, name, login, location, dob,
                   identity, street, coordinates, timezone, registered)


class Importer:

    def __init__(self, curr_session):
        self.curr_session = curr_session

    def days_to_birthday(self, birthday_string):
        '''
        This method is used to determine the number of days until a person's birthday.
        '''
        date_format = '%Y-%m-%d'
        today_date = datetime.strptime(
            datetime.utcnow().strftime(date_format), date_format)
        if birthday_string[5:] == '02-29':
            test_year = datetime.utcnow().year
            for _ in range(4):
                if calendar.isleap(test_year):
                    birthday_string = str(test_year)+birthday_string[4:]
                    birthday = datetime.strptime(birthday_string, date_format)
                    if birthday < today_date:
                        test_year += 4
                    else:
                        break
                else:
                    test_year += 1
        else:
            birthday_string = str(today_date.year) + birthday_string[4:]
            birthday = datetime.strptime(birthday_string, date_format)
            if birthday < today_date:
                birthday_string = str(today_date.year + 1) + birthday_string[4:]
                birthday = datetime.strptime(birthday_string, date_format)
        return (birthday - today_date).days

    def database_content_init(self, record):
        '''
        This method is used to save the full record to the database.
        '''
        date_pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
        record_items = []
        record_items.append(person.Person(
            record['gender'], record['email'], record['phone'],
            record['cell'], record['nat']))
        base_key = record['name']
        record_items.append(name.Name(
            base_key['title'], base_key['first'],
            base_key['last'], record_items[0]))
        base_key = record['location']
        record_items.append(location.Location(
            base_key['city'], base_key['state'], base_key['country'],
            base_key['postcode'], record_items[0]))
        base_key = record['location']['street']
        record_items.append(street.Street(
            base_key['number'], base_key['name'], record_items[2]))
        base_key = record['location']['coordinates']
        record_items.append(coordinates.Coordinates(
            base_key['latitude'], base_key['longitude'], record_items[2]))
        base_key = record['location']['timezone']
        record_items.append(timezone.Timezone(
            base_key['offset'], base_key['description'], record_items[2]))
        base_key = record['login']
        record_items.append(login.Login(
            base_key['uuid'], base_key['username'], base_key['password'],
            base_key['salt'], base_key['md5'], base_key['sha1'],
            base_key['sha256'], record_items[0]))
        base_key = record['dob']
        record_items.append(dob.Dob(
            datetime.strptime(base_key['date'], date_pattern),
            base_key['age'], base_key['days_to_birthday'], record_items[0]))
        base_key = record['registered']
        record_items.append(registered.Registered(
            datetime.strptime(base_key['date'], date_pattern),
            base_key['age'], record_items[0]))
        base_key = record['id']
        record_items.append(identity.Identity(
            base_key['name'], base_key['value'], record_items[0]))
        self.curr_session.add_all(record_items)
        self.curr_session.commit()

    def db_init(self):
        '''
        Method for creating a database and filling it with records.
        If file persons.json doesn't exist it will try to download data
        from https://randomuser.me/api/.
        '''
        if not os.path.exists('test.db'):
            Base.metadata.create_all(engine)
            print('I have created a database')
        if not self.curr_session.query(person.Person).first():
            try:
                with open('persons.json', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                self.helper_function(data)
                print('I have added records to database')
            except IOError:
                print('I find lack of this persons.json file very disturbing!')
                print('But I will try to dowload this data!')
                try:
                    request_session = requests.Session()
                    request_session.head('https://randomuser.me/api/')
                    request = request_session.get(
                        url='https://randomuser.me/api/?results=1000')
                    self.helper_function(request.json())
                    print('I have added records to database')
                except requests.exceptions.RequestException:
                    print('I have failed!')
                    sys.exit()

    def helper_function(self, data):
        for record in data['results']:
            del record['picture']
            record['cell'] = re.sub('[^0-9]', '', record['cell'])
            record['phone'] = re.sub('[^0-9]', '', record['phone'])
            record['dob']['days_to_birthday'] = self.days_to_birthday(
                record['dob']['date'][:10])
            self.database_content_init(record)
