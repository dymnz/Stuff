from flask import Flask, render_template, request, redirect, Response, url_for
from pymongo import MongoClient
from log import *
import daily_operation as do
import storage_operation as so
import customer_operation as co
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

@app.route('/cost')
def cost():
	# serve index template
	date = request.args.get('date')
	all_purchase_list = do.get_purchases_at_date(db, date)

	if all_purchase_list is None or len(all_purchase_list)<=0: 	
		return render_template('cost.html', date=date)

	sum_cost_list = []
	for customer_info in all_purchase_list:
		sum_total = 0
		cost_total = 0
		for purchase in customer_info[1]: 
			purchase['total'] = int(purchase['amount']) * int(purchase['price'])
			purchase['cost_total'] = int(purchase['amount']) * int(purchase['cost'])
			sum_total += purchase['total']
			cost_total += purchase['cost_total']
		sum_cost_list.append((sum_total, cost_total))

	all_purchase_list = zip(all_purchase_list, sum_cost_list)
	return render_template('cost.html', date=date, all_purchase_list=all_purchase_list)

@app.route('/month')
def month():
	# serve index template
	month = request.args.get('month')
	month_purchase_list = co.get_all_month_summary_list(db, month)
	return render_template('month.html', month=month, month_purchase_list=month_purchase_list)


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
		purchase['total'] = int(purchase['amount']) * int(purchase['price'])
		sum_total += purchase['total']

	return (render_template("date_customer.html", date=date, customer=customer, purchase_list=purchase_list, sum_total=sum_total))

@app.route('/cost/customer_profit')
def cost_customer_profit():
	date = request.args.get('date')
	customer = request.args.get('customer')

	purchase_list = do.get_purchases_at_date_of_customer(db, date, customer)

	if purchase_list is None: 
		return render_template('cost.html', date=date)	

	cost_total = 0
	price_total = 0
	profit_total = 0
	for purchase in purchase_list: 
		purchase['cost_total'] = int(purchase['amount']) * int(purchase['cost'])
		cost_total += purchase['cost_total']
		purchase['price_total'] = int(purchase['amount']) * int(purchase['price'])
		price_total += purchase['price_total']
		purchase['profit_total'] = purchase['price_total'] - purchase['cost_total']
		profit_total += purchase['profit_total']

	return (render_template("cost_customer_profit.html", date=date, customer=customer, purchase_list=purchase_list, cost_total=cost_total, price_total=price_total, profit_total=profit_total))

@app.route('/cost/customer')
def cost_customer():
	date = request.args.get('date')
	customer = request.args.get('customer')

	purchase_list = do.get_purchases_at_date_of_customer(db, date, customer)

	if purchase_list is None: 
		return render_template('cost.html', date=date)	

	sum_total = 0
	for purchase in purchase_list: 
		print(purchase)
		purchase['total'] = int(purchase['amount']) * int(purchase['cost'])
		sum_total += purchase['total']

	return (render_template("cost_customer.html", date=date, customer=customer, purchase_list=purchase_list, sum_total=sum_total))


@app.route('/month/customer')
def month_customer():
	month = request.args.get('month')
	customer = request.args.get('customer')
	purchase_list = co.get_customer_month_purchase_list(db, customer, month)

	if purchase_list is None: 
		return render_template('month.html', month=month)	

	sum_total = 0
	for purchase in purchase_list: 
		print(purchase)
		purchase['total'] = int(purchase['amount']) * int(purchase['price'])
		sum_total += purchase['total']

	return (render_template("month_customer.html", month=month, customer=customer, purchase_list=purchase_list, sum_total=sum_total))
	


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

	if url_for('date') in request.referrer:
		return redirect(url_for('date', date=request.form['date']))
	elif url_for('cost') in request.referrer:	
		return redirect(url_for('cost', date=request.form['date']))	
	else:
		return render_template('calendar.html')

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

	if url_for('date_customer') in request.referrer:
		return redirect(url_for('date_customer', date=request.form['date'], customer=request.form['customer']))
	elif url_for('cost_customer') in request.referrer:	
		return redirect(url_for('cost_customer', date=request.form['date'], customer=request.form['customer']))
	elif url_for('cost_customer_profit') in request.referrer:	
		return redirect(url_for('cost_customer_profit', date=request.form['date'], customer=request.form['customer']))	
	elif url_for('month_customer') in request.referrer:	
		split_date = request.form['date'].split('_')
		month = split_date[0] + '_' + split_date[1]
		return redirect(url_for('month_customer', month=month, customer=request.form['customer']))	
	else:
		return render_template('calendar.html')

	return redirect(url_for('date_customer', date=request.form['date'], customer=request.form['customer']))


@app.route('/new_stuff', methods=['POST'])
def new_stuff():
	so.new_stuff(db, 
		request.form['name'], 
		int(request.form['price']),
		int(request.form['cost'])
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
def calendar():
	return render_template('calendar.html')

@app.route('/calendar_cost')
def calendar_cost():
	return render_template('calendar_cost.html')


if __name__ == '__main__':
	app.run('127.0.0.1', '8123')
