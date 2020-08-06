#!/usr/bin/env python3.8

import os
import re
import json
import calendar
from datetime import datetime
from sqlalchemy import create_engine
import base
from model import (coordinates, dob, identity, location, login,
                   name, person, registered, street, timezone)

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

if os.path.exists('test.db'):
    os.remove('test.db')

People_database = create_engine('sqlite:///test.db')

base.Base.metadata.create_all(People_database)

with open('persons.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
for record in data['results']:
    del record['picture']
    record['cell'] = re.sub('[^0-9]', '', record['cell'])
    record['phone'] = re.sub('[^0-9]', '', record['phone'])
    record['dob']['days_to_birthday'] = days_to_birthday(record['dob']['date'][:10])

print(json.dumps(data['results'][0], indent=4))
print(json.dumps(data['results'][338], indent=4))
print(json.dumps(data['results'][648], indent=4))
print(json.dumps(data['results'][657], indent=4))
