from flask import Flask, render_template, request
from pymongo import MongoClient
from configparser import ConfigParser


app = Flask(__name__)

config = ConfigParser()
config.read('config.ini')

client = MongoClient(config['DATABASE']['STRING'])
db = client[config['DATABASE']['DATABASE_NAME']]
collection = db[config['DATABASE']['COLLECTION_LOGIN']]

@app.route('/')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
