from pymongo import MongoClient
from log import *
from manager_test import *
from operation_test import *

# Creating connection to communicate with Mongo DB
client = MongoClient('localhost:27017')
db = client.Shop

# Setup logger
setup_logger()

# manager_test(db)

operation_test(db)

