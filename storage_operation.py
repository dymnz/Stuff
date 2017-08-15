from log import *
import storage_manager as sm

def new_stuff(db, name, price, cost):
	logging.info('New stuff: {}, {}, {}'.format(name, price, cost))
	sm.new_stuff(db, name, price, cost)

def remove_stuff(db, name):
	logging.info('Remove stuff: {}'.format(name))
	sm.remove_stuff(db, name)

def increase_stuff(db, name, change):
	logging.info('Increase stuff: {}, {}'.format(name, change))
	sm.increase_stuff(db, name, change)


def decrease_stuff(db, name, change):
	logging.info('Decrease stuff: {}, {}'.format(name, change))
	sm.decrease_stuff(db, name, change)

def set_stuff_price(db, name, price):
	logging.info('Set stuff price: {}, {}'.format(name, price))
	sm.set_stuff_price(db, name, price)

def get_stuff_list(db):
	stuff_names = sm.get_stuff_names(db)

	if stuff_names is None or len(stuff_names) == 0:
		return None

	all_stuff_list = []
	for name in stuff_names:
		stuff = sm.get_stuff_by_name(db, name)
		
		all_stuff_list.append(stuff)

	return all_stuff_list
