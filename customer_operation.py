import customer_manager as cm


def get_all_month_summary_list(db, month):
	customer_names = cm.get_customer_names(db)

	month_summary_list = []
	for customer_name in customer_names: 
		month_purchase_list = cm.get_purchases_at_month(db, customer_name, month)

		if (month_purchase_list is None) or len(month_purchase_list)==0:
			continue

		sum_total = 0
		for purchase in month_purchase_list:
			sum_total += purchase['amount'] * purchase['price']


		month_summary_list.append((customer_name, sum_total))

	return month_summary_list

def get_customer_month_purchase_list(db, customer, month):
	month_purchase_list = cm.get_purchases_at_month(db, customer, month)

	return month_purchase_list


def get_all_month_purchase_list(db, month):
	customer_names = cm.get_customer_names(db)

	month_purchase_list = []
	for customer_name in customer_names: 
		month_purchase_list = cm.get_purchases_at_month(db, customer_name, month)

		if (month_purchase_list is None) or len(month_purchase_list)==0:
			continue			
			
		month_purchase_list.append((customer_name, month_purchase_list))

	return month_purchase_list



