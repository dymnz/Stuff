from log import *
import customer_manager as cm
import storage_manager as sm
import daily_manager as dm

# CM #################################################
def add_customer_test(db):
	cm.add_customer(db, 'cus_1', '00001', 'cus_1@g.com')
	name_list = cm.get_customer_names(db)
	print(name_list)

	cm.add_customer(db, 'cus_2', '00002', 'cus_2@g.com')
	name_list = cm.get_customer_names(db)
	print(name_list)

	cm.add_customer(db, 'cus_2', '00002', 'cus_2@g.com')
	name_list = cm.get_customer_names(db)
	print(name_list)
	
	cm.add_customer(db, 'cus_1', '00001', 'cus_1@g.com')
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

	cm.add_purchase(db, cus_1['name'], '2017_8_9', 'shit_2', 7, 12)
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

def get_purchases_of_date_test(db):
	purchase_list = cm.get_purchases_at_date(db, 'cus_1', '2017_8_8')
	print(purchase_list)
	print(purchase_list[0]['purchases'])

	purchase_list = cm.get_purchases_at_date(db, 'cus_1', '2017_8_9')
	print(purchase_list)

	purchase_list = cm.get_purchases_at_date(db, 'cus_1', '2017_8_11')
	print(purchase_list)
	if len(purchase_list) == 0:
		print('Empty list')

def remove_purchase_test(db):
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)

	cm.remove_purchase(db, cus_1['name'], '2017_8_8', 'shit_1', 100, 10)	
	cus_1 = cm.get_customer_by_name(db, 'cus_1')
	print(cus_1)


# SM #################################################
def add_stuff_test(db):	
	sm.new_stuff(db, 'stu_1', 100)
	name_list = sm.get_stuff_names(db)
	print(name_list)

	stu_1 = sm.get_stuff_by_name(db, 'stu_1')
	print(stu_1)

	sm.increase_stuff(db, 'stu_1', 10)	
	stu_1 = sm.get_stuff_by_name(db, 'stu_1')
	print(stu_1)

	sm.decrease_stuff(db, 'stu_1', 10)	
	stu_1 = sm.get_stuff_by_name(db, 'stu_1')
	print(stu_1)

	name_list = sm.get_stuff_names(db)
	print(name_list)

	sm.delete_stuff(db, 'stu_1')
	name_list = sm.get_stuff_names(db)
	print(name_list)

def set_stuff_price_test(db):
	sm.new_stuff(db, 'stu_2', 100)
	stu_2 = sm.get_stuff_by_name(db, 'stu_2')
	print(stu_2)

	sm.set_stuff_price(db, stu_2['name'], 999)
	stu_2 = sm.get_stuff_by_name(db, 'stu_2')
	print(stu_2)

# DM #################################################
def add_entry_test(db):
	dm.add_daily_entry(db, '2017_8_10')
	date_list = dm.get_daily_entry_dates(db)
	print(date_list)

	dm.add_daily_entry(db, '2017_8_10')
	date_list = dm.get_daily_entry_dates(db)
	print(date_list)

	dm.remove_daily_entry(db, '2017_8_10')
	date_list = dm.get_daily_entry_dates(db)
	print(date_list)

def add_customer_daily_test(db):
	dm.add_daily_entry(db, '2017_8_11')
	date_list = dm.get_daily_entry_dates(db)
	print(date_list)

	dm.add_customer(db, '2017_8_11', 'cus_1')
	date_1 = dm.get_daily_entry_by_date(db, '2017_8_11')
	print(date_1)

	dm.add_customer(db, '2017_8_11', 'cus_2')
	date_1 = dm.get_daily_entry_by_date(db, '2017_8_11')
	print(date_1)

	dm.add_customer(db, '2017_8_11', 'cus_1')
	date_1 = dm.get_daily_entry_by_date(db, '2017_8_11')
	print(date_1)

	dm.remove_customer(db, '2017_8_11', 'cus_2')
	date_1 = dm.get_daily_entry_by_date(db, '2017_8_11')
	print(date_1)
	dm.remove_customer(db, '2017_8_11', 'cus_1')
	date_1 = dm.get_daily_entry_by_date(db, '2017_8_11')
	print(date_1)

def manager_test(db):
	# # CM test
	add_customer_test(db)
	add_purchase_test(db)
	get_purchases_of_date_test(db)
	add_customer_test(db)
	remove_purchase_test(db)

	# # SM test
	# add_stuff_test(db)
	# set_stuff_price_test(db)

	# DM test
	# add_entry_test(db)
	# add_customer_daily_test(db)
