from flask import Flask, render_template, request, redirect, Response
from pymongo import MongoClient
from log import *
import daily_operation as do
import json

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.Shop



@app.route('/show')
def show_date():
	# serve index template
	date = request.args.get('date')
	all_purchase_list = do.get_purchases_at_date(db, date)
	sum_total_list = []
	print(all_purchase_list)
	for customer_info in all_purchase_list:
		sum_total = 0
		for purchase in customer_info[1]: 
			print(purchase)
			purchase['total'] = int(purchase['amount']) * int(purchase['price'])
			sum_total += purchase['total']
		sum_total_list.append(sum_total)

	all_purchase_list = zip(all_purchase_list, sum_total_list)
	return render_template('date.html', date=date, all_purchase_list=all_purchase_list)

@app.route('/new_purchase', methods=['POST'])
def new_purchase():
	do.new_purchase(db, 
		request.form['date'], 
		request.form['customer'], 
		request.form['stuff'],
		int(request.form['amount']),
		int(request.form['price']))
	return render_template('date.html', date=request.form['date'], all_purchase_list=do.get_purchases_at_date(db, request.form['date']))

@app.route('/')
def show_calendar():
	return render_template('calendar.html')


if __name__ == '__main__':
	app.run('127.0.0.1', '8123')
