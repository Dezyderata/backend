#!/usr/bin/env python3.8

import os
import re
import json
import calendar
from datetime import datetime
from base import Session, engine, Base
from model import (person, name, login, location, dob,
                   identity, street, coordinates, timezone, registered)

def days_to_birthday(birthday_string):
    date_format = '%Y-%m-%d'
    today_date = datetime.strptime(datetime.utcnow().strftime(date_format), date_format)
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

def database_content_init(record, session):
    record_items = []
    record_items.append(person.Person(record['gender'], record['email'], record['phone'],
                                      record['cell'], record['nat']))
    base_key = record['name']
    record_items.append(name.Name(base_key['title'], base_key['first'], base_key['last'],
                                  record_items[0]))
    base_key = record['location']
    record_items.append(location.Location(base_key['city'], base_key['state'], base_key['country'],
                                          base_key['postcode'], record_items[0]))
    base_key = record['location']['street']
    record_items.append(street.Street(base_key['number'], base_key['name'], record_items[2]))
    base_key = record['location']['coordinates']
    record_items.append(coordinates.Coordinates(base_key['latitude'], base_key['longitude'],
                                                record_items[2]))
    base_key = record['location']['timezone']
    record_items.append(timezone.Timezone(base_key['offset'], base_key['description'],
                                          record_items[2]))
    base_key = record['login']
    record_items.append(login.Login(base_key['uuid'], base_key['username'], base_key['password'],
                                    base_key['salt'], base_key['md5'], base_key['sha1'],
                                    base_key['sha256'], record_items[0]))
    base_key = record['dob']
    record_items.append(dob.Dob(base_key['date'], base_key['age'], base_key['days_to_birthday'],
                                record_items[0]))
    base_key = record['registered']
    record_items.append(registered.Registered(base_key['date'], base_key['age'], record_items[0]))
    base_key = record['id']
    record_items.append(identity.Identity(base_key['name'], base_key['value'], record_items[0]))
    session.add_all(record_items)
    session.commit()

if not os.path.exists('test.db'):
    Base.metadata.create_all(engine)
    print('I created a database')
session = Session()
if session.query(person.Person).first() is None:
    with open('persons.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    for record in data['results']:
        del record['picture']
        record['cell'] = re.sub('[^0-9]', '', record['cell'])
        record['phone'] = re.sub('[^0-9]', '', record['phone'])
        record['dob']['days_to_birthday'] = days_to_birthday(record['dob']['date'][:10])
        database_content_init(record, session)
    print('I added records to databade')
session.close()
