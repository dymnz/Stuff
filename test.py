from pymongo import MongoClient

def insert():
	try:
		employeeId = input('Enter Employee id :')
		employeeName = input('Enter Name :')
		employeeAge = input('Enter age :')
		employeeCountry = input('Enter Country :')
			
		db.Employees.insert_one({
			"id": employeeId,
			"name":employeeName,
			"age":employeeAge,
			"country":employeeCountry
		})
		print('\nInserted data successfully\n')
	
	except Exception as e:
		print(str(e))

def read():
	try:
		empCol = db.Employees.find()
		print('\n All data from EmployeeData Database \n')
		for emp in empCol:
			print(emp)

	except Exception as e:
		print(str(e))

def update():
	try:
		db.Employees.update_one(
		  { 
		  	"id": "123",
		  	"name": "john"
		  	 },
		  {
		    "$set": {
		      "country": "JP"
		    }
		  }
		)
	except Exception as e:
		print(str(e))

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

#insert()
read()
update()
read()
