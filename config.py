import argparse
from datetime import date, datetime
from base import Session
import importer
import controller

class Config:

    def __init__(self):
        self.date_format = '%Y-%m-%d'
        self.curr_session = Session()
        self.curr_importer = importer.Importer(self.curr_session)
        self.curr_importer.db_init()
        self.curr_controller = controller.Controller(self.curr_session)
        self.parser = argparse.ArgumentParser()

    def cli(self):
        self.parser.add_argument(
            '-gp', '--gender_percent', action='store_true',
            help='''Prints percentage of each gender in database.
            No arguments necessary''')
        self.parser.add_argument(
            '-aa', '--average_age', action='store_true',
            help='''Prints global average age and average for each gender.
            No arguments necessary''')
        self.parser.add_argument(
            '-bp', '--best_passwd', action='store_true',
            help='''Prints best password base on a few contition like length.
            No arguments necessary''')
        self.parser.add_argument(
            '-pc', '--most_popular_cities', type=int,
            help='''Prints list of most popular cities in database.
            Require one integer argument to determent list length''')
        self.parser.add_argument(
            '-pp', '--most-common-passwords', type=int,
            help='''Prints list of most popular passwords in database.
            Require one integer argument to determent list length''')
        self.parser.add_argument(
            '-bb', '--born_between',
            type=lambda s: datetime.strptime(s, self.date_format), nargs=2,
            help='''Prints list of people born between two dates.
            Require two arguments in format "YYYY-MM-DD".''')

    def run(self):
        self.cli()
        args = self.parser.parse_args()
        if args.gender_percent:
            self.curr_controller.gender_percent()
        if args.average_age:
            self.curr_controller.average_age()
        if args.best_passwd:
            self.curr_controller.best_password()
        if args.most_popular_cities:
            self.curr_controller.most_popular_cities(args.most_popular_cities)
        if args.most_common_passwords:
            self.curr_controller.most_popular_passwords(args.most_common_passwords)
        if args.born_between:
            self.curr_controller.born_between(args.born_between[0], args.born_between[1])
        print("Thank you for your cooperation. Bye Bye!")
        self.curr_session.close()
