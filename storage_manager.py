from log import *

def new_stuff(db, name, price):
	try: 
		db.Storage.insert_one({
			'name': name,
			'amount': 0,
			'price': price
		})
		logging.debug('New stuff: {}, {}'.format(name, price))

	except Exception as e:
		logging.error('Error new stuff: {}, {}, {}'.format(name, price))
		logging.error(e)

def delete_stuff(db, name):
	try: 
		db.Storage.delete_one(
			{'name': name}
		)
		logging.debug('Removed stuff: {}'.format(name))
	except Exception as e:
		logging.error('Error removing stuff: {}'.format(name))
		logging.error(e)	

def increase_stuff(db, name, change):
	try: 
		db.Storage.update_one(
			{'name': name},
			{'$inc': {
				'amount': change
			}}
		)
		logging.debug('Added stuff: {}, {}'.format(name, change))

	except Exception as e:
		logging.error('Error adding stuff: {}, {}'.format(name, change))
		logging.error(e)

def decrease_stuff(db, name, change):
	try: 
		db.Storage.update_one(
			{'name': name},
			{'$inc': {
				'amount': -change
			}}
		)
		logging.debug('Decreased stuff: {}, {}'.format(name, change))

	except Exception as e:
		logging.error('Error decreasing stuff: {}, {}'.format(name, change))
		logging.error(e)

def set_stuff_price(db, name, price):
	try: 
		db.Storage.update_one(
			{'name': name},
			{'$set': {
				'price': price
			}}
		)
		logging.debug('Set stuff price: {}, {}'.format(name, price))

	except Exception as e:
		logging.error('Error setting stuff price: {}, {}'.format(name, price))
		logging.error(e)

def get_stuff_by_name(db, name):
	return db.Storage.find_one({'name': name});

def get_stuff_names(db):	
	stuffs = db.Storage.find({}, {'_id': 0, 'name': 1})
	name_list = []
	for stuff in stuffs:
		name_list.append(stuff['name'])
	
	return name_list


