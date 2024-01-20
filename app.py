from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from configparser import ConfigParser


app = Flask(__name__)

config = ConfigParser()
config.read('config.ini')

client = MongoClient(config['DATABASE']['STRING'])
db = client[config['DATABASE']['DATABASE_NAME']]
collection_login = db[config['DATABASE']['COLLECTION_LOGIN']]


@app.route('/', methods=['GET', 'POST'])
def login():
        return render_template('index.html')


@app.route("/loginsuccessfull", methods=["GET", "POST"])
def validate_login():
    error_message = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)

        required_one = {
            "_id": username, "password": password
        }

        data = collection_login.find_one(required_one)
        print(data)

        if data:
            return render_template('dashboard.html')
        else:
            error_message = "Invalid Username and password"
            return render_template('index.html')

    return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug = True)

