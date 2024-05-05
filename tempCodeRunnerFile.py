from flask import Flask, render_template, request, send_file, jsonify
from pymongo import MongoClient
import requests
import joblib
import smtplib
import pandas as pd
from openai import OpenAI
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from docx import Document
from datetime import datetime
import os

config = ConfigParser()
config.read('config.ini')

app = Flask(__name__)
openai_client = OpenAI(api_key="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")

translate_api_url = config['URL']['TRANSLATE_URL']
chatbot_api_url = config['URL']['CHATBOT_URL']


model = joblib.load('static/models/disease_prediction_model.joblib')
le_results = joblib.load('static/models/label_encoder_results.joblib')

    
client = MongoClient(config['DATABASE']['STRING'])
db = client[config['DATABASE']['DATABASE_NAME']]
collection_pl = db[config['DATABASE']['COLLECTION_PATIENT_LOGIN']]
collection_dl = db[config['DATABASE']['COLLECTION_DOCTOR_LOGIN']]
collection_data = db[config['DATABASE']['COLLECTION_DATA']]
collection_as = db[config['DATABASE']['COLLECTION_APPOINTMENT_STATUS']]
collection_a = db[config['DATABASE']['COLLECTION_APPOINTMENT']]
collection_pi = db[config['DATABASE']['COLLECTION_PATIENT_INFORMATION']]
collection_di = db[config['DATABASE']['COLLECTION_DOCTOR_INFORMATION']]
collection_c = db[config['DATABASE']['COLLECTION_CONSULTATION']]