from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from configparser import ConfigParser
import certifi
ca = certifi.where()

config = ConfigParser()
config.read('config.ini')

client = MongoClient('mongodb+srv://karthikr:admin@cluster0.xvrddw5.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client['Vaidhya']
collection_login = db['login']

username = 'karthik'
password = 'karthik'

required_one = {
    '_id': username, 'password': password
 }

data = collection_login.find_one(required_one)
print(data)