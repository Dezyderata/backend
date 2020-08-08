import re
from datetime import datetime
from sqlalchemy import func
from model import (person, login, location, dob)

class Controller:

    def __init__(self, curr_session):
        self.curr_session = curr_session

    def gender_percent(self):
        genders_counted = self.curr_session.query(
            person.Person.gender, func.count(
                person.Person.gender)).group_by(
                    person.Person.gender).all()
        people_gen = 0
        for gen in genders_counted:
            people_gen += gen[1]
        print(people_gen)
        for gen in genders_counted:
            print(f'Percent of {gen[0]}: {(gen[1]/people_gen)*100}%')

    def average_age(self):
        all_age = self.curr_session.query(func.avg(dob.Dob.age)).all()
        print(f'Average age of all people in db: {all_age[0][0]:.2f}')
        age_by_gender = self.curr_session.query(
            person.Person.gender, func.avg(dob.Dob.age)).filter(
                person.Person.person_id == dob.Dob.person_id).group_by(
                    person.Person.gender).all()
        for gen in age_by_gender:
            print(f'Average age for {gen[0]}: {gen[1]:.2f}')

    def most_popular_cities(self, number):
        cities_list = self.curr_session.query(
            location.Location.city, func.count(location.Location.city)).group_by(
                location.Location.city).order_by(
                    func.count(location.Location.city).desc(),
                    location.Location.city.asc()).limit(number).all()
        for city in cities_list:
            print(f'{city[0]}: {city[1]}')

    def most_popular_passwords(self, number):
        passwords_list = self.curr_session.query(
            login.Login.password, func.count(login.Login.password)).group_by(
                login.Login.password).order_by(
                    func.count(login.Login.password).desc(),
                    login.Login.password.asc()).limit(number).all()
        for passwd in passwords_list:
            print(f'{passwd[0]}: {passwd[1]}')

    def born_between(self, start_date, stop_date):
        people_between = self.curr_session.query(
            login.Login.username).filter(
                login.Login.person_id == dob.Dob.person_id, dob.Dob.date.between(
                    start_date, stop_date)).all()
        for item in people_between:
            print(item[0])

    def best_password(self):
        passwords = self.curr_session.query(login.Login.password).distinct().all()
        best_score = 0
        best_pass = ''
        for passwd, in passwords:
            score = 0
            if re.search('[a-z]', passwd):
                score += 1
            if re.search('[A-Z]', passwd):
                score += 2
            if re.search('[0-9]', passwd):
                score += 1
            if len(passwd) > 7:
                score += 5
            if re.search('[^a-zA-Z0-9\\s]', passwd):
                score += 3
            if score > best_score:
                best_score = score
                best_pass = passwd
                print(f'New best password: {best_pass} with score: {best_score}')
        print(f'Best password: {best_pass} with score: {best_score}')
