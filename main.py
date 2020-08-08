#!/usr/bin/env python3.8

from base import Session
import importer
import controller

curr_session = Session()
curr_importer = importer.Importer(curr_session)
curr_importer.db_init()
curr_controller = controller.Controller(curr_session)
curr_controller.average_age()
curr_controller.best_password()
curr_controller.gender_percent()
curr_controller.most_popular_cities(5)
curr_controller.most_popular_passwords(9)
curr_controller.born_between('1966-01-01', '1967-01-01')
curr_session.close()
