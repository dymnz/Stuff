from flask import Flask, render_template, request, redirect, Response, url_for
from pymongo import MongoClient
from log import *
import daily_operation as do
import storage_operation as so
import json

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.Shop
setup_logger()

@app.route('/date')
def date():
	# serve index template
	date = request.args.get('date')
	all_purchase_list = do.get_purchases_at_date(db, date)

	if all_purchase_list is None or len(all_purchase_list)<=0: 	
		return render_template('date.html', date=date)

	sum_total_list = []
	
	for customer_info in all_purchase_list:
		sum_total = 0
		for purchase in customer_info[1]: 
			purchase['total'] = int(purchase['amount']) * int(purchase['price'])
			sum_total += purchase['total']
		sum_total_list.append(sum_total)

	all_purchase_list = zip(all_purchase_list, sum_total_list)
	return render_template('date.html', date=date, all_purchase_list=all_purchase_list)

@app.route('/date/customer')
def date_customer():
	date = request.args.get('date')
	customer = request.args.get('customer')

	print('customer: {}'.format(customer))

	purchase_list = do.get_purchases_at_date_of_customer(db, date, customer)

	if purchase_list is None: 
		return render_template('date.html', date=date)	

	sum_total = 0
	for purchase in purchase_list: 
		print(purchase)
		purchase['total'] = int(purchase['amount']) * int(purchase['price'])
		sum_total += purchase['total']

	return (render_template("date_customer.html", date=date, customer=customer, purchase_list=purchase_list, sum_total=sum_total))


@app.route('/new_purchase', methods=['POST'])
def new_purchase():
	do.new_purchase(db, 
		request.form['date'], 
		request.form['customer'], 
		request.form['stuff'],
		int(request.form['amount']))
	
	all_purchase_list = do.get_purchases_at_date(db, request.form['date'])

	if all_purchase_list is None: 
		return render_template('date.html', date=request.form['date'])

	sum_total_list = []
	
	for customer_info in all_purchase_list:
		sum_total = 0
		for purchase in customer_info[1]: 
			purchase['total'] = int(purchase['amount']) * int(purchase['price'])
			sum_total += purchase['total']
		sum_total_list.append(sum_total)

	all_purchase_list = zip(all_purchase_list, sum_total_list)
	return redirect(url_for('date', date=request.form['date']))

@app.route('/storage')
def show_storage():
	all_stuff_list = so.get_stuff_list(db)
	return render_template('storage.html', all_stuff_list=all_stuff_list )


@app.route('/remove_purchase', methods=['POST'])
def remove_purchase():
	do.remove_purchase(db, 
		request.form['date'], 
		request.form['customer'], 
		request.form['stuff'],
		int(request.form['amount']),
		int(request.form['price']))
	return redirect(url_for('date_customer', date=request.form['date'], customer=request.form['customer']))


@app.route('/new_stuff', methods=['POST'])
def new_stuff():
	so.new_stuff(db, 
		request.form['name'], 
		int(request.form['price'])
	)
	return redirect(url_for('show_storage'))

@app.route('/increase_stuff', methods=['POST'])
def increase_stuff():
	so.increase_stuff(db, 
		request.form['name'], 
		int(request.form['amount'])
	)
	return redirect(url_for('show_storage'))

@app.route('/remove_stuff', methods=['POST'])
def remove_stuff():
	so.remove_stuff(db, 
		request.form['name']
	)
	return redirect(url_for('show_storage'))		
	
@app.route('/')
def show_calendar():

	return render_template('calendar.html')


if __name__ == '__main__':
	app.run('127.0.0.1', '8123')
