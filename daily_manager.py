from log import *

def add_daily_entry(db, date):
	try: 
		db.Daily.update(
			{'date': date},
			{
			"$setOnInsert": 
				{"date": date,
				 'customers': []}
			},
			upsert = True
		)
		logging.debug('Added daily entry {}'.format(date))

	except Exception as e:
		logging.error('Error adding daily entry {}'.format(date))
		logging.error(e)

def remove_daily_entry(db, date):
	try: 
		db.Daily.delete_one(
			{'date': date}
		)
		logging.debug('Removed daily entry {}'.format(date))
	except Exception as e:
		logging.error('Error removing daily entry {}'.format(date))
		logging.error(e)	


def add_customer(db, date, name):
	try: 
		db.Daily.update(
			{'date': date },
			{ '$addToSet': {
				'customers': name
			}}
		)
		logging.debug('Added customer at entry: {}, {}'.format(date, name))

	except Exception as e:
		logging.error('Error adding customer at entry: {}, {}'.format(date, name))
		logging.error(e)	

def remove_customer(db, date, name):
	try: 
		db.Daily.update_one(
			{'date': date},
			{'$pull': {
				'customers': name
			}}
		)
		logging.debug('Removed customer at entry: {}, {}'.format(date, name))

	except Exception as e:
		logging.error('Error removing customer at entry: {}, {}'.format(date, name))
		logging.error(e)	

def get_daily_entry_by_date(db, date):
	return db.Daily.find_one({'date': date});

def get_daily_entry_dates(db):	
	entries = db.Daily.find({}, {'_id': 0, 'date': 1})
	date_list = []
	for entry in entries:
		date_list.append(entry['date'])

	return date_list
