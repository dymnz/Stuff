from log import *
import daily_operation as do
import customer_operation as co


def get_month_summary_list_test(db):
	co.get_month_summary_list(db, '2017_7')

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
	# new_purchase_test(db)
	# remove_purchase_test(db)
	get_month_summary_list_test(db)
