#!/usr/bin/env python3.8

import argparse
from datetime import date, datetime
from base import Session
import importer
import controller

date_format = '%Y-%m-%d'
curr_session = Session()
curr_importer = importer.Importer(curr_session)
curr_importer.db_init()
curr_controller = controller.Controller(curr_session)

parser = argparse.ArgumentParser()
parser.add_argument('-g_p', '--gender_percent', action='store_true',
                    help='''Prints percentage of each gender in database.
                    No arguments necessary''')
parser.add_argument('-a_a', '--average_age', action='store_true',
                    help='''Prints global average age and average for each gender.
                    No arguments necessary''')
parser.add_argument('-b_p', '--best_passwd', action='store_true',
                    help='''Prints best password base on a few contition like length.
                    No arguments necessary''')
parser.add_argument('-p_c', '--popular_cities', type=int,
                    help='''Prints list of most popular cities in database.
                    Require one integer argument to determent list length''')
parser.add_argument('-p_p', '--popular_pass', type=int,
                    help='''Prints list of most popular passwords in database.
                    Require one integer argument to determent list length''')
parser.add_argument('-b_b', '--born_between',
                    type=lambda s: datetime.strptime(s, date_format), nargs=2,
                    help='''Prints list of people born between two dates.
                    Require two arguments in format "YYYY-MM-DD".''')
args = parser.parse_args()
if args.gender_percent:
    curr_controller.gender_percent()
elif args.average_age:
    curr_controller.average_age()
elif args.best_passwd:
    curr_controller.best_password()
elif args.popular_cities:
    curr_controller.most_popular_cities(args.popular_cities)
elif args.popular_pass:
    curr_controller.most_popular_passwords(args.popular_pass)
elif args.born_between:
    curr_controller.born_between(args.born_between[0], args.born_between[1])
else:
    print("Thank you for your cooperation. Bye Bye!")
curr_session.close()
