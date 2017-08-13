from log import *
import daily_operation as do
import daily_manager as dm

def new_purchase_test(db):
	do.new_purchase(db, '2017_8_8', 'cus_1', 'stu_1', 100, 3)
	print(do.get_purchases_at_date(db, '2017_8_8'))

	do.new_purchase(db, '2017_8_8', 'cus_2', 'stu_2', 99, 2)
	print(do.get_purchases_at_date(db, '2017_8_8'))

	do.new_purchase(db, '2017_8_8', 'cus_1', 'stu_3', 98, 1)
	print(do.get_purchases_at_date(db, '2017_8_8'))

def remove_purchase_test(db):
	do.remove_purchase(db, '2017_8_8', 'cus_1', 'stu_3', 98, 1)
	print(do.get_purchases_at_date(db, '2017_8_8'))

	do.remove_purchase(db, '2017_8_8', 'cus_2', 'stu_2', 99, 2)
	print(do.get_purchases_at_date(db, '2017_8_8'))



def operation_test(db):
	new_purchase_test(db)
	remove_purchase_test(db)
