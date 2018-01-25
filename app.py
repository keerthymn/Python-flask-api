from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#creating an engine for connection to the database 
#cars.db should be in the main project folder
e = create_engine('sqlite:///cars.db')


app = Flask(__name__)
api = Api(app)

#class for returning a car by its id given
class car_by_id(Resource):
	def get(self,car_id):
		#connecting to database
		con = e.connect()
		#execute the query and results saved in query
		query = con.execute("select make,model,year,id,last_updated from cars \
			where id = '%s'"%car_id)
		result = {'car':[dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
		return result

#class returns all cars in the database when the request is GET
#class inserts a new column to the database when request is POST 
class all_cars(Resource):
	def get(self):
		#connecting to database
		con = e.connect()
		#execute the query and results saved in query
		query = con.execute("select make,model,year,id,last_updated from cars")
		return {'cars': [dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
	def post(self):
		#getting the data from curl to req_data
		req_data = request.get_json()
		#initialising
		make = ""
		model = ""
		year = ""
		chassis_id = ""
		price = ""
		car_id = ""
		last_updated = ""
		#getting each value from req_data
		if "make" in req_data:
			make = req_data["make"]
		if "model" in req_data:
			model = req_data["model"]			
		if "year" in req_data:
			year = req_data["year"]
		if "chassis_id" in req_data:
			chassis_id = req_data["chassis_id"]
		if "price" in req_data:
			price = req_data["price"]
		if "last_updated" in req_data:
			last_updated = req_data["last_updated"]
		if "car_id" in req_data:
			car_id = req_data["id"]
		#connect to database
		con = e.connect()
		#inserting into database
		query = con.execute("insert into cars values ('%s','%s','%s','%s',\
			'%s','%s','%s')"
			%(make,model,year,chassis_id,car_id,last_updated,price))
		return "201 created"

#class finds the average price of a car when make,model and year is given
class find_avgprice(Resource):
	def post(self):
		#getting the data from curl to req_data
		req_data = request.get_json()
		#initializing
		make = ""
		model = ""
		year = ""
		#getting each value from req_data
		if "make" in req_data:
			make = req_data["make"]
		if "model" in req_data:
			model = req_data["model"]			
		if "year" in req_data:
			year = req_data["year"]
		#connecting to database
		con = e.connect()
		#calculating average from the query results
		total = 0
		count = 0
		for row in con.execute("select price from cars where make = '%s' and model = \
			'%s' and year = '%s'"%(make,model,year)):
			total = total + float(row[0])
			count = count + 1
		avg = total/count
		return 'avg_price:{}'.format(avg)



api.add_resource(find_avgprice,'/avgprice')
api.add_resource(car_by_id,'/car/<string:car_id>') 
api.add_resource(all_cars,'/car')


if __name__ == '__main__':
	app.run(debug = True)
