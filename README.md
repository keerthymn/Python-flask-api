# Python-flask-api
A simple Python flask API using sqlite.

This project uses Python, Flask Web framework, Flask-Restful extension, SQLite3 and SQLAlchemy.
I am using Windows, some commands may vary for other Operating Systems.

The project is an API with GET and POST requests and uses an SQLite database which is created from a CSV file attached.
The CSV file contains details about cars.

Requirements

Flask documentations suggests to use a virtualenv for using flask applications so that we can use Python for other projects besides Flask-based web applications. So lets start by installing virtualenv. 

Open command prompt and use the following command to install virtualenv.

$ pip install virtualenv

Now create a folder for the project

$ mkdir api-project
$ cd api-project
$ virtualenv venv
$ venv\Scripts\activate

We are in the main folder of the project. Now install the requirements using the following commands.

$ pip install flask
$ pip install flask-restful
$ pip install sqlalchemy

Database

Now to get the database in sqlite3 from the CSV file, the following commands can be used

$ sqlite3 <path>\cars.db
sqlite> .mode csv
sqlite> .import <path>/cars.csv cars
    
Running the application.

Save app.py in the api-project folder and run it using the following command

$ python app.py

This command should successfully run the api. 

For testing I used Postman application initially and for curl I used git-bash
Open git-bash and type in the curl and it gives you the response. You can also open the request URL in a browser and it will give you the output.

Examples curl
•	$ curl http://localhost:5000/car/2
Output:
    "car": [
        {
            "model": "Fiesta",
            "id": "2",
            "last_updated": "2017-03-01 00:00:00",
            "year": "2002",
            "make": "Ford"
        }
    ]
}

•	$ curl http://localhost:5000/car

Output: 

    "cars": [
        {
            "model": "Micra",
            "id": "1",
            "last_updated": "2017-02-01 00:00:00",
            "year": "2004",
            "make": "Nissan"
        },
        {
            "model": "Micra",
            "id": "1",
            "last_updated": "2017-03-01 00:00:00",
            "year": "2004",
            "make": "Nissan"
        },
        {
            "model": "Fiesta",
            "id": "2",
            "last_updated": "2017-03-01 00:00:00",
            "year": "2002",
            "make": "Ford"
        },
        {
            "model": "A3",
            "id": "3",
            "last_updated": "2017-04-01 00:00:00",
            "year": "",
            "make": "Audi"
        },
        {
            "model": "Micra",
            "id": "4",
            "last_updated": "2017-05-01 00:00:00",
            "year": "2004",
            "make": "Nissan"
        },
        {
            "model": "308",
            "id": "5",
            "last_updated": "2017-06-01 00:00:00",
            "year": "1998",
            "make": "Peugeot"
        },
    ]
}


•	$ curl --data '{"make":"Nissan","model":"Micra", "year":"2004"}' --header "Content-Type:application/json" --request POST http://localhost:5000/avgprice

Output:
"avg_price:366.6666666666667"

•	$ curl -H "Content-Type: application/json" -X POST http://localhost:5000/car -d '{"make":"Seat","model":"Cordoba","year":"2003","chassis_id":"12345F"}'

Output:
"201 created"



References:
•	https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
•	https://prettyprinted.com/courses


