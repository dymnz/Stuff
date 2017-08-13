from pymongo import MongoClient


client = MongoClient('localhost:27017')
print(client.database_names())
client.drop_database('Shop')
print(client.database_names())