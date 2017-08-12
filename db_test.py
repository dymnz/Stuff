from log import *
import customer_manager as cm
import storage_manager as sm
import json

def add_customer_test(db):
	cm.add_customer(db, 'cus_1', '00001', 'cus_1@g.com')
	name_list = cm.get_customer_names(db)
	print(name_list)

	cm.add_customer(db, 'cus_2', '00002', 'cus_2@g.com')
	name_list = cm.get_customer_names(db)
	print(name_list)


def add_purchase_test(db):
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

	cm.add_purchase(db, cus_1['name'], '2017_8_8', 'shit_1', 100, 10)
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

	cm.add_purchase(db, cus_1['name'], '2017_8_8', 'shit_2', 7, 12)
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

def remove_purchase_test(db):
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

	cm.remove_purchase(db, cus_1['name'], '2017_8_8', 'shit_1', 100, 10)	
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

