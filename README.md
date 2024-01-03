# FoodBankSoftware

## Instructions for running this software:

These instructions were adapted from the following tutorial: https://www.youtube.com/watch?v=7LNl2JlZKHA.

## A few pointers for getting set up
if you are missing any pakages 

Try:

Install to homebrew https://www.youtube.com/watch?v=IWJKRmFLn-g&t=3s

Add brew to  to path or ~/.zshrc for Mac:

	$ vim ~/.zshrc
 
	add this line to your zshrc -> export PATH=${PATH}:/opt/homebrew/bin
 
	save then exit 
 
	$ source  ~/.zshrc)


Assume you are activating Python 3 venv:

  $ brew install mysql pkg-config 
  
  $ pip install mysqlclient
  
  $ pip install flask-mysqldb
  

Before running the Server Edit the Sql configuration information in the connections.py file inside the flask-server folder

  - app.config['MySQL_HOST'] = 'localhost' 
  - app.config["MYSQL_USER"] = "root"   
  - app.config["MYSQL_PASSWORD"] = "YourLocalHostMySqlPassword"
  - app.config["MYSQL_DB"] = "foodbankdb"

Finally Make sure to download foodbankdb.sql into your database in order to make use of our application



## Backend

### On MacOS:
Create and setup virtual python environment:
```
cd flask-server
python3 -m venv venv
source venv/bin/activate
pip3 install Flask
```

Run the server:

```
python3 server.py
```

### On Windows
Create and setup virtual python environment:
```
cd flask-server
python -m venv venv
./venv/Scripts/activate
pip install Flask
```

Run the server:
```
python server.py
```

## Frontend
Start the react app by running:
```
cd client
npm start
```
