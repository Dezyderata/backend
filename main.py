#!/usr/bin/env python3.8

import os
from sqlalchemy import create_engine
from model import *
import base

if os.path.exists('test.db'):
    os.remove('test.db')

people_database = create_engine('sqlite:///test.db')

base.Base.metadata.create_all(people_database)
