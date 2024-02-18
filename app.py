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
# import shutil
# import os

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
collection_login = db[config['DATABASE']['COLLECTION_LOGIN']]
collection_doctor_login = db[config['DATABASE']['COLLECTION_DOCTOR_LOGIN']]
collection_data = db[config['DATABASE']['COLLECTION_DATA']]

main_username = ""


@app.route('/')
def login():
    # def empty_directory(directory):
    #     shutil.rmtree(directory)
    #     os.mkdir(directory)

    # # Example usage:
    # directory_to_empty = 'static/documentsgen'
    # empty_directory(directory_to_empty)

    return render_template('index.html')

@app.route('/index')
def index():
    # def empty_directory(directory):
    #     shutil.rmtree(directory)
    #     os.mkdir(directory)

    # # Example usage:
    # directory_to_empty = 'static/documentsgen'
    # empty_directory(directory_to_empty)
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aboutk')
def aboutk():
    return render_template('aboutk.html')

@app.route('/diseasePrediction')
def diseasePrediction():
    return render_template('2options.html')

@app.route('/prediction1')
def prediction1():
    return render_template('prediction.html')

@app.route('/mcq')
def mcq():
    return render_template('mcq.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/predic')
def predic():
    return render_template('predic.html')

@app.route("/predict2")
def predict2():
    return render_template('prediction.html')

@app.route("/doctorLogin")
def doctorLogin():
    # def empty_directory(directory):
    #     shutil.rmtree(directory)
    #     os.mkdir(directory)

    # # Example usage:
    # directory_to_empty = 'static/documentsgen'
    # empty_directory(directory_to_empty)
    return render_template('doctorLogin.html')

@app.route("/doctordashboard")
def doctordashboard():
    return render_template("doctordashboard.html")

@app.route("/emailsent", methods=["POST"])
def emailsent():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        sender_email = config['EMAIL']['SENDER_EMAIL']
        sender_password = config['EMAIL']['SENDER_PASSWORD']
        to_email = config['EMAIL']['RECEIVER_EMAIL']
        subject = "Response form Vaidhya"
        body = f"Sender Name: {name}\nSender Email: {email}\nMessage: {message}"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        return render_template('about.html')


@app.route('/ask', methods=['POST'])
def ask():
    questions = request.get_json().get('question')
    response = requests.post(f"{chatbot_api_url}/input_bot", json={'questions': questions})
    if response.status_code == 200:
        answers = response.json().get('answer')
        return jsonify({'answers': answers})
    else:
        return jsonify({'error': 'Failed to get answers'})

@app.route('/mcqfun1', methods=["GET", "POST"])
def mcqfun1():
    q1 =request.form["q1"]
    q2 =request.form["q2"]
    q3 =request.form["q3"]
    q4 =request.form["q4"]
    q5 =request.form["q5"]
    q6 =request.form["q6"]
    q7 =request.form["q7"]
    q8 =request.form["q8"]
    q9 =request.form["q9"]
    q10 =request.form["q10"]

    input_data = {
    'age': 22,  # Example age value
    'Your friend has invited you to a party. Consider how you might respond in the given scenario. Choose the option that best reflects your feelings and tendencies': q1,
    'You have an upcoming deadline at work. How do you typically handle this': q2,
    'You receive unexpected praise for your achievements. How do you react?': q3,
    'You witness a car accident on the street. How does it affect you?': q4,
    'You are preparing for a social event with friends. How do you approach it?': q5,
    'You find yourself in a crowded and noisy environment. How do you react?': q6,
    'You encounter a trigger related to a past traumatic event. How do you cope?': q7,
    'You are faced with a decision that requires careful consideration. How do you approach it?': q8,
    'You are experiencing a period of heightened creativity and productivity. How does it impact you?': q9,
    'You are in a situation where you feel judged by others. How do you react?': q10
    }

    # Map categorical answers to numerical values (assuming a to g)
    answer_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

    # Apply the mapping to convert categorical answers to numerical values
    for mcq, answer in input_data.items():
        if mcq != 'age':  # Skip 'age' column
            input_data[mcq] = answer_mapping.get(answer, 0)  # Use 0 for unknown answers

    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])

    # Make predictions on the input data
    predictions = model.predict(input_df.iloc[:, 1:])  # Exclude the 'Results' column

    # Decode predictions if label encoding was used during training
    predictions_decoded = le_results.inverse_transform(predictions)

    symptom = predictions_decoded[0]

    existing_student = collection_data.find_one({'_id': main_username})
    if existing_student:
        
        collection_data.update_one(
            
            {'_id': main_username},
            {'$set': {'symptom-test': symptom}}
        )      
        
    return render_template('predic.html', symp = symptom)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    texts = data.get('texts', [])
    target_lang = data.get('target_lang', 'en')

    response = requests.post(f"{translate_api_url}/translate", json={'texts': texts, 'target_lang': target_lang})

    if response.status_code == 200:
        translated_texts = response.json().get('translated_texts', [])
        return jsonify({'translated_texts': translated_texts})
    else:
        return jsonify({'error': 'Failed to get translation'})


@app.route("/loginsuccessfull", methods=["GET", "POST"])
def validate_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        required_one = {
            "_id": username, "password": password
        }
        data = collection_login.find_one(required_one)
        if data:
            global main_username
            main_username = username
            return render_template('dashboard.html')
        else:
            return render_template('index.html')
    return render_template('index.html')

@app.route("/userfeeling", methods=["GET", "POST"])
def userfeeling():
    if request.method == "POST":
        userfeeling = request.form["feeling"]


        completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Consider the given feeling, analyze it and classify it into one of these categories: None, Depression, Anxiety Disorders, Schizophrenia, Bipolar Disorder, Obsessive-Compulsive Disorder (OCD), and Post-Traumatic Stress Disorder (PTSD). Give me only the name of the label, not the explanation."},
                {"role": "user", "content": userfeeling}
            ]
        )

        symptom = completion.choices[0].message.content
        print(symptom)


        existing_student = collection_data.find_one({'_id': 'karthik'})
        if existing_student:
            
            collection_data.update_one(
                
                {'_id': main_username},
                {'$set': {'symptom-feel': symptom}}
            )      

        return render_template('prediction.html', symptom = symptom)
    else:
        return render_template('prediction.html', symptom = None)

@app.route("/doctorloginsuccessfull", methods=["GET", "POST"])
def validate_doctor_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        required_one = {
            "_id": username, "password": password
        }
        data = collection_doctor_login.find_one(required_one)
        if data:
            return render_template('doctordashboard.html')
        else:
            return render_template('doctorLogin.html')
    return render_template('doctorLogin.html')

@app.route('/fetchpatientdetails', methods=["GET", "POST"])
def fetchpatientdetails():
        
        patientid =" "
        patientname =" "
        patientage =" "
        sfeel = " "
        stest = " "
        message = "Data Not Available"
        doc_name = " "
        doc_id = " "

        if request.method == "POST":
            patientid = request.form["patientid"]
            key = request.form["key"]

            required_one = {
                "patientid": patientid,
                "key": key
            }

            data = collection_data.find_one(required_one)

            if data:
                message = "Data Found!"
                patientid = data["patientid"]
                patientname = data["patientname"]
                patientage = data["age"]
                sfeel = data["symptom-feel"]
                stest = data["symptom-test"]
                doc_name = data["doctor_name"]
                doc_id = data["doctor_id"]

                return render_template("doctordashboard.html", message = message, name = patientname, pid = patientid, age = patientage, sfeel = sfeel, stest = stest, doc_name = doc_name, doc_id = doc_id)

            else:
                return render_template("doctordashboard.html", message = message, name = patientname, pid = patientid, age = patientage, sfeel = sfeel, stest = stest, doc_name = doc_name, doc_id = doc_id)

@app.route('/generatereport', methods=["GET", "POST"])
def generatereport():
    data = request.json
    now = datetime.now()
    current_month = str(now.month)
    current_date = str(now.day)
    current_year = str(now.year)

    data['DD'] = current_date
    data['MM'] = current_month
    data['YYYY'] = current_year

    doc = Document('static/documents/patient_report.docx')

    # Replace placeholders with actual data
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace('{{' + key + '}}', str(value))
    fname = data["pid"]
    temp_docx_path = f'static/documentsgen/{fname}.docx'
    doc.save(temp_docx_path)
    # doc.save(f'C:/Users/karth/Downloads/{fname}.docx')

    return send_file(temp_docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug = True)

