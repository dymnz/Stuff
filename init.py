from pymongo import MongoClient
from log import *
from db_test import *

# Creating connection to communicate with Mongo DB
client = MongoClient('localhost:27017')
db = client.Shop

# Setup logger
setup_logger()

# Tests
add_customer_test(db)
add_purchase_test(db)
remove_purchase_test(db)
