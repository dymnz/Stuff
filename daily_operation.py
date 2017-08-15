from log import *
import customer_manager as cm
import storage_manager as sm
import daily_manager as dm

def new_purchase(db, date, customer, stuff, amount):

	price = sm.get_stuff_by_name(db, stuff)['price']

	logging.info('New purchase: {}, {}, {}, {}, {}'.format(date, customer, stuff, amount, price))

	cm.add_customer(db, customer, None, None)
	cm.add_purchase(db, customer, date, stuff, amount, price)
	dm.add_daily_entry(db, date)
	dm.add_customer(db, date, customer)
	sm.decrease_stuff(db, stuff, amount)


def remove_purchase(db, date, customer, stuff, amount, price):
	logging.info('Remove purchase: {}, {}, {}, {}, {}'.format(date, customer, stuff, amount, price))

	cm.remove_purchase(db, customer, date, stuff, amount, price)
	sm.increase_stuff(db, stuff, amount)

	purchase_list = cm.get_purchases_at_date(db, customer, date)
	if len(purchase_list) == 0:
		logging.info('No other purchase: {}, {}'.format(date, customer))
		dm.remove_customer(db, date, customer)

def get_purchases_at_date(db, date):
	entry = dm.get_daily_entry_by_date(db, date)

	if entry is None or len(entry) == 0:
		return None

	all_purchase_list = []
	for customer in entry['customers']:
		purchase_list = cm.get_purchases_at_date(db, customer, date)
		purchase_list = purchase_list[0]['purchases']
		all_purchase_list.append((customer, purchase_list))

	return all_purchase_list

def get_purchases_at_date_of_customer(db, date, customer):
	entry = dm.get_daily_entry_by_date(db, date)

	if entry is None or len(entry) == 0:
		return None

	if customer not in entry['customers']:
		return None

	purchase_list = cm.get_purchases_at_date(db, customer, date)

	if purchase_list is None:
		return None

	return purchase_list[0]['purchases']

	


