from log import *

def add_customer(db, name, phone, email):
	try: 
		db.Customer.insert_one({
			'name': name,
			'phone': phone,
			'email': email,
			'purchases': []
		})
		logging.info('Added customer {}, {}, {}'.format(name, phone, email))

	except Exception as e:
		logging.error('Error adding customer {}, {}, {}'.format(name, phone, email))
		logging.error(e)

def add_purchase(db, name, date, stuff, amount, price):
	try: 
		db.Customer.update_one(
			{'name': name},
			{'$push': {
				'purchases': {
					'date': date,
					'stuff': stuff,
					'amount': amount,
					'price': price
			}}}
		)
		logging.info('Added purchase {}, {}, {}, {}, {}'.format(name, date, stuff, amount, price))
	except Exception as e:
		logging.error('Error adding purchase {}, {}, {}, {}, {}'.format(name, date, stuff, amount, price))
		logging.error(e)

def remove_purchase(db, name, date, stuff, amount, price):
	try: 
		db.Customer.update_one(
			{'name': name},
			{'$pull': {
				'purchases': {
					'date': date,
					'stuff': stuff,
					'amount': amount,
					'price': price
			}}}
		)
		logging.info('Removed purchase {}, {}, {}, {}, {}'.format(name, date, stuff, amount, price))
	except Exception as e:
		logging.error('Error removing purchase {}, {}, {}, {}, {}'.format(name, date, stuff, amount, price))
		logging.error(e)	

def get_customer_by_name(db, name):
	return db.Customer.find_one({'name': name});

def get_customer_names(db):	
	customers = db.Customer.find({}, {'_id': 0, 'name': 1})
	name_list = []
	for customer in customers:
		name_list.append(customer['name'])
	
	return name_list


