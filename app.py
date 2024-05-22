from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for
from pymongo import MongoClient
import requests
import joblib
import smtplib
import pandas as pd
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from docx import Document
from datetime import datetime, timedelta, timezone
import os
import random

config = ConfigParser()
config.read('config.ini')

app = Flask(__name__)

app.secret_key = config['SECRETS']['APP_SECRET_KEY']

translate_api_url = config['URL']['TRANSLATE_URL']
chatbot_api_url = config['URL']['CHATBOT_URL']
feel_api_url = config['URL']['FEEL_URL']


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
collection_o = db[config['DATABASE']['OTP']]
collection_n = db[config['DATABASE']['NUMBERS']]

main_patientusername = ""
main_doctorusername=""
# main_patientname = ""
main_doctorname=""
# main_doctorid=""
# main_patientid=""
# main_doctorid=""
temp_username = ""
gemail=""
new_username=""
new_email=""
docnew_username=""
docnew_email=""

ALLOWED_ROUTES = ['/index']

def allowed_route(route):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if route in ALLOWED_ROUTES:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('error_404'))
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

@app.route('/error')
# @allowed_route('/error')
def error_404():
    return render_template('error.html'), 404

@app.route('/errorfetch')
# @allowed_route('/error')
def error_500():
    return render_template('errorfetch.html'), 500

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
    return render_template('doctorLogin.html')

@app.route("/doctordashboard")
def doctordashboard():
    return render_template("doctordashboard.html")

@app.route("/appointments")
def appointments():
    return render_template("appointment.html")

@app.route("/patientReport")
def patientReport():
    return render_template("patientReport.html")

@app.route("/docappointment")
def docappointment():
    return render_template("docappointment.html")

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("forgotpassword.html")

@app.route("/otp")
def otp():
    return render_template("otp.html")

@app.route("/createpassword")
def createpassword():
    return render_template("createpassword.html")

@app.route("/docforgotpassword")
def docforgotpassword():
    return render_template("docforgotpassword.html")

@app.route("/docotp")
def docotp():
    return render_template("docotp.html")

@app.route("/doccreatepassword")
def doccreatepassword():
    return render_template("createpassword.html")

@app.route("/newusername")
def newusername():
    return render_template("newusername.html")

@app.route("/newotp")
def newotp():
    return render_template("newotp.html")

@app.route('/newemail')
def newemail():
    return render_template("newemail.html")

@app.route("/createnewpassword")
def createnewpassword():
    return render_template("createnewpassword.html")

@app.route("/docnewusername")
def docnewusername():
    return render_template("docnewusername.html")

@app.route('/docnewemail')
def docnewemail():
    return render_template("docnewemail.html")

@app.route("/docnewotp")
def docnewotp():
    return render_template("docnewotp.html")

@app.route("/doccreatenewpassword")
def doccreatenewpassword():
    return render_template("doccreatenewpassword.html")

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

    existing_student = collection_data.find_one({'_id': main_patientusername})
    if existing_student:
        
        collection_data.update_one(
            
            {'_id': main_patientusername},
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
        data = collection_pl.find_one(required_one)
        if data:
            global main_patientusername, main_doctorname
            main_patientusername = username
            try:
                patient_info = collection_pi.find_one({ 'patient_username' : username})
                patient_id = patient_info['_id']
                consultation = collection_c.find_one({ '_id' : patient_id})
                doctor_id = consultation['doctor_id']
                doctor_info = collection_di.find_one({'_id' : doctor_id})
                main_doctorname = doctor_info['doctor_name']
            except:
                 pass
            
            if not collection_pi.find_one({'patient_username': main_patientusername}):
                return render_template('patientinfo.html')

            return render_template('dashboard.html')
        else:
            return render_template('index.html')
    return render_template('index.html')

@app.route("/userfeeling", methods=["GET", "POST"])
def userfeeling():
    if request.method == "POST":
        userfeeling = request.form["feeling"]

        try:
            response = requests.post(f"{feel_api_url}/feel_bot", json={'question': userfeeling})
            if response.status_code == 200:
                answer = response.json().get('answer')
            symptom = answer
            existing_student = collection_data.find_one({'_id': main_patientusername})
            if existing_student:
                
                collection_data.update_one(
                    {'_id': main_patientusername},
                    {'$set': {'symptom-feel': symptom}}
                )      
        
        except:
            return render_template('prediction.html', symptom = "Error 429!")
        
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
        data = collection_dl.find_one(required_one)
        if data:
            global main_doctorusername
            main_doctorusername = username

            if not collection_di.find_one({'doctor_username': main_doctorusername}):
                return render_template('doctorinfo.html')

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

                return render_template("patientReport.html", message = message, name = patientname, pid = patientid, age = patientage, sfeel = sfeel, stest = stest, doc_name = doc_name, doc_id = doc_id)

            else:
                return render_template("patientReport.html", message = message, name = patientname, pid = patientid, age = patientage, sfeel = sfeel, stest = stest, doc_name = doc_name, doc_id = doc_id)

@app.route('/generatereport', methods=["GET"])
def generatereport():
    name = request.args.get('name')
    pid = request.args.get('pid')
    age = request.args.get('age')
    sfeel = request.args.get('sfeel')
    stest = request.args.get('stest')
    docid = request.args.get('docid')
    docname = request.args.get('docname')

    data = {'name': name, 'pid': pid, 'age': age, 'sfeel': sfeel, 'stest': stest, 'doctor_id': docid, 'doctor_name': docname}

    now = datetime.now()
    current_month = str(now.month)
    current_date = str(now.day)
    current_year = str(now.year)

    data['DD'] = current_date
    data['MM'] = current_month
    data['YYYY'] = current_year

    doc = Document('static/documents/patient_report.docx')

    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace('{{' + key + '}}', str(value))

    # Ensure the directory exists
    documentsgen_dir = os.path.join(app.root_path, 'static', 'documentsgen')
    os.makedirs(documentsgen_dir, exist_ok=True)

    fname = data["pid"]
    temp_docx_path = os.path.join(documentsgen_dir, f'{fname}.docx')
    doc.save(temp_docx_path)

    return send_file(temp_docx_path, as_attachment=True)

@app.route('/appointment')
def appointment():
    def get_next_weekdays(start_date, num_days):
        weekdays = []
        current_date = start_date

        while len(weekdays) < num_days:
            current_date += timedelta(days=1)
            if current_date.weekday() >= 5:
                current_date += timedelta(days=(7 - current_date.weekday()))

            weekdays.append(current_date)

        return weekdays
    
    def get_availability(date):
        availability = collection_as.find_one({"_id": date})
        if availability:
            return availability
        else:
            return None

    today = datetime.today()
    next_weekdays = get_next_weekdays(today, 5)
    dates = [date.strftime("%d-%m-%Y") for date in next_weekdays]

    dates_with_availability = []
    print(main_doctorname)
    for date in dates:
        availability = get_availability(date)
        if availability:
            slots_availability = {key: value for key, value in availability.items() if key != '_id'}
            dates_with_availability.append((date, slots_availability))
    return render_template('appointment.html', dates_with_availability=dates_with_availability, doctor_name = main_doctorname)

@app.route('/appointment/submitted',methods=['POST', 'GET'])
def submit_appointment():

    appointment_data = request.get_json(force=True)  

    name = appointment_data.get('name')
    pid = appointment_data.get('pid')
    time_slot = appointment_data.get('timeSlot')
    mode = appointment_data.get('mode')
    date = appointment_data.get('dates')


    query = {"_id" : date} 
    newquery = {"$set" : {time_slot : 1}} 
    collection_as.update_one(query, newquery)

    new_appointment = {
        "_id" : f"{pid}_{date}_{time_slot}",
        "name": name,
        "patient_username": pid,
        "time_slot": time_slot,
        "mode" : mode,
        "date" : date
    }

    collection_a.insert_one(new_appointment)


    sender_email = config['EMAIL']['SENDER_EMAIL']
    sender_password = config['EMAIL']['SENDER_PASSWORD']

    try:
        
        patient_info = collection_pi.find_one({ 'patient_username' : pid})
        patient_id = patient_info['_id']

        patient_email = patient_info['email']

        consultation = collection_c.find_one({ '_id' : patient_id})
        doctor_id = consultation['doctor_id']
        doctor_info = collection_di.find_one({'_id' : doctor_id})

        doctor_email = doctor_info['email']

    except:
        response_data = {"message": "Something Went Wrong! Try Again"}
        return jsonify(response_data)        

    subject_p = f"Appointment Confirmation: Your Upcoming Visit with Dr. {doctor_info['doctor_name']}"
    subject_d = f"Appointment Scheduled: Your Upcoming Visit with Mr. {patient_info['patient_name']}"

    body_p = f"Dear {patient_info['patient_name']},\n\nWe hope this email finds you well.\n\nWe are writing to confirm your scheduled appointment with Dr. {doctor_info['doctor_name']} on {date} between {time_slot} IST.\n\nLocation: {doctor_info['location']}\nAddress: {doctor_info['consultation_address']}\nRoom/Office: {doctor_info['room']}\n\nPlease arrive 10-15 minutes before your scheduled appointment time to complete any necessary paperwork.In case of online mode Papers will be sent via Email.\n\nIf you need to reschedule or cancel your appointment, please let us know at least 24 hours in advance so we can accommodate other patients.\n\nWe look forward to seeing you on {date}. If you have any questions or concerns in the meantime, please don't hesitate to contact us.\n\nBest regards,\nVaidhya."

    body_d = f"Dear Dr. {doctor_info['doctor_name']}\n\nI hope this message finds you well.\n\nThis email is to confirm the upcoming appointment scheduled for {patient_info['patient_name']}, who is {patient_info['age']} years old, with you on {date} between {time_slot}. The appointment will be held in your given location.\n\nPatient Details:\n\nName: {patient_info['patient_name']}\nAge: {patient_info['age']}\nDate: {date}\nTime: {time_slot}\nMode: {mode}\nEmail: {patient_info['email']}\nPh_Nuber: {patient_info['ph_number']}\n\nPlease ensure that all necessary arrangements are made for the appointment.\n\nThank you for your attention to this matter.\n\nBest regards,\nVaidhya."

    message_p = MIMEMultipart()
    message_p['From'] = sender_email
    message_p['To'] = patient_email
    message_p['Subject'] = subject_p
    message_p.attach(MIMEText(body_p, 'plain'))

    message_d = MIMEMultipart()
    message_d['From'] = sender_email
    message_d['To'] = doctor_email
    message_d['Subject'] = subject_d
    message_d.attach(MIMEText(body_d, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, patient_email, message_p.as_string())
        server.sendmail(sender_email, doctor_email, message_d.as_string())


    response_data = {"message": "Appointment submitted successfully!"}
    return jsonify(response_data)

@app.route('/docappointment/submitted',methods=['POST', 'GET'])
def submit_docappointment():
    appointment_docdata = request.get_json() 
    if appointment_docdata:
        if not appointment_docdata['timeSlots'] and not appointment_docdata['customTimeSlot']:
                response_data = {"message": "Select Atleast One Time slot!"}
                return jsonify(response_data)
        
        datek = datetime.strptime(appointment_docdata['date'], "%Y-%m-%d")
        date = datek.strftime("%d-%m-%Y")
        time_slots = []
        result={'_id':date}


        for time_slot in appointment_docdata.get('timeSlots', []):
            time_slots.append(time_slot)

        if appointment_docdata['customTimeSlot']:
            time = appointment_docdata['customTimeSlot']['from'] + " - " + appointment_docdata['customTimeSlot']['to'] + " IST"
            time_slots.append(time)
        
        def check_overlap(time1, time2):
            start1, end1 = map(lambda x: int(x.split(':')[0])*60 + int(x.split(':')[1].split()[0]), time1.split(' - '))
            start2, end2 = map(lambda x: int(x.split(':')[0])*60 + int(x.split(':')[1].split()[0]), time2.split(' - '))
            
            if start1 <= start2 <= end1 or start1 <= end2 <= end1:
                return True
            if start2 <= start1 <= end2 or start2 <= end1 <= end2:
                return True
            return False
        
        for i in range(len(time_slots)):
            for j in range(i+1, len(time_slots)):
                if check_overlap(time_slots[i], time_slots[j]):
                        response_data = {"message": "Select the Time Slots Such that they don't overlap with each other"}
                        return jsonify(response_data)
                
        for t_s in time_slots:
            result[t_s] = 0
            
        
        if collection_as.find_one({ '_id' : date}):
            collection_as.delete_one({ '_id' : date})

        collection_as.insert_one(result)

        response_data = {"message": "Appointments Offerd Successfully!"}
        return jsonify(response_data)
        
    else:
        response_data = {"message": "Something Went Wrong!"}
        return jsonify(response_data)

@app.route("/forgotpassword/datafound", methods=['POST', 'GET'])
def forgotpassworddatafound():
    username = request.form["login-username"] #take name entity

    if collection_pl.find_one({'_id': username}) or collection_pl.find_one({'email': username}):
        pin = int(''.join(random.choices('0123456789', k=6)))

        if collection_pl.find_one({'_id': username}):
            data = collection_pl.find_one({'_id': username})
            email = data['email']
        else:
            data = collection_pl.find_one({'email': username})
            email = data['email']


        sender_email = config['EMAIL']['SENDER_EMAIL']
        sender_password = config['EMAIL']['SENDER_PASSWORD']
        to_email = email
        subject = "One Time Password"
        body = f"Your One Time Password is {pin}.\n\nThe OTP will be valid only for 10 minutes.\n\nRegards,\nVaidhya"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())

        collection_o.create_index("createdAt", expireAfterSeconds=600)

        to_push = {
            "createdAt": datetime.now(timezone.utc),
            '_id': email,
            'otp': pin
        }

        if collection_o.find_one({'_id': email}):
            query = {'_id': email} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
            newquery = {"$set" : {"otp" : pin}} # for update
            collection_o.update_one(query, newquery)
        else:
            collection_o.insert_one(to_push)
        global temp_username
        temp_username = username
        
        return render_template("otp.html")
    else:
        return render_template("forgotpassword.html", message="Invalid username or email")

@app.route("/otpverified", methods=['POST', 'GET'])
def otpverified():

    one = request.form["input1"]
    two = request.form["input2"]
    three = request.form["input3"]
    four = request.form["input4"]
    five = request.form["input5"]
    six = request.form["input6"]

    pin = int(one+two+three+four+five+six)

    make_data = collection_pl.find_one({"_id": temp_username})
    email = make_data['email']

    make_datax = collection_o.find_one({"_id": email})

    otp_from_mongo = make_datax['otp']
    if otp_from_mongo == pin:
        return render_template("createpassword.html")
    else:
        return render_template("otp.html", message="Invalid OTP")

@app.route("/createpasswordsuccessfull", methods=['POST', 'GET'])
def createpasswordsuccessfull():
    appointment_data = request.get_json()

    password1 = appointment_data['password1']
    password2 = appointment_data['password2']

    print(password1, password2)

    if password1 != password2:
        print(password1, password2)
        return jsonify(message="Password did not match !")
    else:
        if collection_pl.find_one({"_id": temp_username}):
            query = {'_id': temp_username} 
            new_query = {"$set": {"password": password1}} 
            collection_pl.update_one(query, new_query)
            return jsonify(message="Password Changed Successfully !")
        return render_template('error.html')


@app.route("/docforgotpassword/docdatafound", methods=['POST', 'GET'])
def docforgotpassworddatafound():
    username = request.form["login-username"]

    if collection_dl.find_one({'_id': username}) or collection_dl.find_one({'email': username}):
        pin = int(''.join(random.choices('0123456789', k=6)))

        if collection_dl.find_one({'_id': username}):
            data = collection_dl.find_one({'_id': username})
            email = data['email']
        else:
            data = collection_dl.find_one({'email': username})
            email = data['email']


        sender_email = config['EMAIL']['SENDER_EMAIL']
        sender_password = config['EMAIL']['SENDER_PASSWORD']
        to_email = email
        subject = "One Time Password"
        body = f"Your One Time Password is {pin}.\n\nThe OTP will be valid only for 10 minutes.\n\nRegards,\nVaidhya"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())

        collection_o.create_index("createdAt", expireAfterSeconds=600)

        to_push = {
            "createdAt": datetime.now(timezone.utc),
            '_id': email,
            'otp': pin
        }

        if collection_o.find_one({'_id': email}):
            query = {'_id': email} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
            newquery = {"$set" : {"otp" : pin}} # for update
            collection_o.update_one(query, newquery)
        else:
            collection_o.insert_one(to_push)
        global temp_doc_username
        temp_doc_username = username
        
        return render_template("docotp.html")
    else:
        return render_template("docforgotpassword.html", message="Invalid Credentials")

@app.route("/docotpverified", methods=['POST', 'GET'])
def docotpverified():

    one = request.form["input1"]
    two = request.form["input2"]
    three = request.form["input3"]
    four = request.form["input4"]
    five = request.form["input5"]
    six = request.form["input6"]

    pin = int(one+two+three+four+five+six)

    make_data = collection_dl.find_one({"_id": temp_doc_username})
    email = make_data['email']
    make_datax = collection_o.find_one({"_id": email})

    otp_from_mongo = make_datax['otp']
    if otp_from_mongo == pin:
        return render_template("doccreatepassword.html")
    else:
        return render_template("docotp.html", message="Invalid OTP")

@app.route("/doccreatepasswordsuccessfull", methods=['POST', 'GET'])
def doccreatepasswordsuccessfull():
    appointment_data = request.get_json()

    password1 = appointment_data['password1']
    password2 = appointment_data['password2']

    print(password1, password2)

    if password1 != password2:
        print(password1, password2)
        return jsonify(message="Password did not match !")
    else:
        if collection_dl.find_one({"_id": temp_doc_username}):
            query = {'_id': temp_doc_username} 
            new_query = {"$set": {"password": password1}} 
            collection_dl.update_one(query, new_query)
            return jsonify(message="Password Changed Successfully !")
        return render_template('error.html')
    
@app.route('/chooseusername',methods=['POST', 'GET'])
def chooseusername():
    username = request.form["login-username"]
    if collection_pl.find_one({'_id': username}):
        return render_template("newusername.html", message="username alreay exist!")
    else:
        global new_username
        new_username = username
        return render_template("newemail.html")

@app.route('/chooseemail',methods=['POST', 'GET'])
def chooseemail():
    email = request.form["login-username"]
    if collection_pl.find_one({'email': email}):
        return render_template("newemail.html", message="email already registered!")
    else:
        global new_email
        new_email = email

        pin = int(''.join(random.choices('0123456789', k=6)))

        sender_email = config['EMAIL']['SENDER_EMAIL']
        sender_password = config['EMAIL']['SENDER_PASSWORD']
        to_email = new_email
        subject = "One Time Password"
        body = f"Your One Time Password is {pin}.\n\nThe OTP will be valid only for 10 minutes.\n\nRegards,\nVaidhya"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())

        collection_o.create_index("createdAt", expireAfterSeconds=600)

        to_push = {
            "createdAt": datetime.now(timezone.utc),
            '_id': new_email,
            'otp': pin
        }

        if collection_o.find_one({'_id': new_email}):
            query = {'_id': new_email} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
            newquery = {"$set" : {"otp" : pin}} # for update
            collection_o.update_one(query, newquery)
        else:
            collection_o.insert_one(to_push)

        return render_template("newotp.html")

@app.route('/newotpverified',methods=['POST', 'GET'])
def newotpverified():
        
        one = request.form["input1"]
        two = request.form["input2"]
        three = request.form["input3"]
        four = request.form["input4"]
        five = request.form["input5"]
        six = request.form["input6"]

        pin = int(one+two+three+four+five+six)
        print(new_email)
        make_datax = collection_o.find_one({"_id": new_email})

        otp_from_mongo = make_datax['otp']

        if otp_from_mongo == pin:
            return render_template("createnewpassword.html")
        else:
            return render_template("newotp.html", message="Invalid OTP")
        
@app.route('/createaccount',methods=['POST', 'GET'])
def createacount():        
    appointment_data = request.get_json()

    password1 = appointment_data['password1']
    password2 = appointment_data['password2']

    if password1 != password2:
        print(password1, password2)
        return jsonify(message="Password did not match !")
    else:
        account = {
            '_id':new_username,
            'email':new_email,
            'password': password1
        }
        collection_pl.insert_one(account)
        return jsonify(message="Account Created Successfully !")

@app.route('/savedetails', methods=['POST', 'GET'])
def savedetails():
    appointment_data = request.get_json()

    if not collection_pi.find_one({'patient_username' : main_patientusername}):

        date = appointment_data['DOB']

        date_object = datetime.strptime(date, '%Y-%m-%d')

        formatted_date = date_object.strftime('%d-%m-%Y')

        dob_date = datetime.strptime(formatted_date, '%d-%m-%Y')
        current_date = datetime.now()
        agek = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))

        mongo = collection_n.find_one({'_id':'patient-register-number'})
        mongox = collection_pl.find_one({'_id':main_patientusername})

        value = mongo['value']
        query = {'_id': "patient-register-number"} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
        newquery = {"$set" : {"value" : value + 1}} # for update
        collection_n.update_one(query, newquery)

        p_id = "VP" + str(value+1)
        patient_username = main_patientusername
        DOB = str(formatted_date)
        age = agek
        address = appointment_data['address']
        blood_group = appointment_data['bloodgroup']
        ph_number = appointment_data['contactnumber']
        email = mongox['email']
        patient_name = appointment_data['name']

        data = {
        "_id" : p_id,
        "patient_username" : patient_username,
        "DOB" : DOB,
        "age" : age,
        "address" : address,
        "blood_group" : blood_group,
        "ph_number" : ph_number,
        "email" : email,
        "patient_name" : patient_name
        }

        print(data)

        collection_pi.insert_one(data)

        return jsonify(message="Details Saved successfully!")
    
    else:
        date = appointment_data['DOB']
        date_object = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_object.strftime('%d-%m-%Y')
        dob_date = datetime.strptime(formatted_date, '%d-%m-%Y')
        current_date = datetime.now()
        agek = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))

        DOB = str(formatted_date)
        age = agek
        address = appointment_data['address']
        blood_group = appointment_data['bloodgroup']
        ph_number = appointment_data['contactnumber']
        patient_name = appointment_data['name']

        query = {'patient_username' : main_patientusername}
        newquery = {"$set" : {"DOB" : DOB, "age" : age, "address" : address, "blood_group" : blood_group, "ph_number" : ph_number, "patient_name" : patient_name}} 
        collection_pi.update_one(query, newquery)

        return jsonify(message="Data Updated successfully!")


@app.route('/docchooseusername',methods=['POST', 'GET'])
def docchooseusername():
    username = request.form["login-username"]
    if collection_dl.find_one({'_id': username}):
        return render_template("docnewusername.html", message="username alreay exist!")
    else:
        global docnew_username
        docnew_username = username
        print(docnew_username)
        return render_template("docnewemail.html")
    
@app.route('/docchooseemail',methods=['POST', 'GET'])
def docchooseemail():
    email = request.form["login-username"]
    if collection_dl.find_one({'email': email}):
        return render_template("docnewemail.html", message="email already registered!")
    else:
        global docnew_email
        docnew_email = email

        pin = int(''.join(random.choices('0123456789', k=6)))

        sender_email = config['EMAIL']['SENDER_EMAIL']
        sender_password = config['EMAIL']['SENDER_PASSWORD']
        to_email = email
        subject = "One Time Password"
        body = f"Your One Time Password is {pin}.\n\nThe OTP will be valid only for 10 minutes.\n\nRegards,\nVaidhya"
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())

        collection_o.create_index("createdAt", expireAfterSeconds=600)

        to_push = {
            "createdAt": datetime.now(timezone.utc),
            '_id': email,
            'otp': pin
        }

        if collection_o.find_one({'_id': email}):
            query = {'_id': email} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
            newquery = {"$set" : {"otp" : pin}} # for update
            collection_o.update_one(query, newquery)
        else:
            collection_o.insert_one(to_push)

        return render_template("docnewotp.html")

@app.route('/docnewotpverified',methods=['POST', 'GET'])
def docnewotpverified():
        one = request.form["input1"]
        two = request.form["input2"]
        three = request.form["input3"]
        four = request.form["input4"]
        five = request.form["input5"]
        six = request.form["input6"]

        pin = int(one+two+three+four+five+six)

        make_datax = collection_o.find_one({"_id": docnew_email})

        otp_from_mongo = make_datax['otp']

        if otp_from_mongo == pin:
            print("Hello")
            return render_template("doccreatenewpassword.html")
        else:
            return render_template("docnewotp.html", message="Invalid OTP")

@app.route('/doccreateaccount',methods=['POST', 'GET'])
def doccreateacount(): 
    print("Hello World")       
    appointment_data = request.get_json()

    password1 = appointment_data['password1']
    password2 = appointment_data['password2']

    if password1 != password2:
        print(password1, password2)
        return jsonify(message="Password did not match !")
    else:
        account = {
            '_id':docnew_username,
            'email':docnew_email,
            'password': password1
        }
        collection_dl.insert_one(account)
        return jsonify(message="Account Created Successfully !")
    
@app.route('/docsavedetails', methods=['POST', 'GET'])
def docsavedetails():
    appointment_data = request.get_json()

    if not collection_di.find_one({'doctor_username' : main_doctorusername}):

        date = appointment_data['DOB']

        date_object = datetime.strptime(date, '%Y-%m-%d')

        formatted_date = date_object.strftime('%d-%m-%Y')

        dob_date = datetime.strptime(formatted_date, '%d-%m-%Y')
        current_date = datetime.now()
        agek = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))

        mongo = collection_n.find_one({'_id':'doctor-register-number'})
        mongox = collection_dl.find_one({'_id':main_doctorusername})

        value = mongo['value']
        query = {'_id': "doctor-register-number"}
        newquery = {"$set" : {"value" : value + 1}}
        collection_n.update_one(query, newquery)

        d_id = "VD" + str(value+1)
        doctor_username = main_doctorusername
        DOB = str(formatted_date)
        age = agek
        address = appointment_data['address']
        blood_group = appointment_data['bloodgroup']
        ph_number = appointment_data['contactnumber']
        email = mongox['email']
        doctor_name = appointment_data['name']
        room = appointment_data['consultancyroomnumber']
        location = appointment_data['consultancylocation']
        consultation_address = appointment_data['consultancyaddress']
        licence_number = appointment_data['licence']
        aadhar = appointment_data['aadhar']




        data = {
        "_id" : d_id,
        "doctor_username" : doctor_username,
        "DOB" : DOB,
        "age" : age,
        "address" : address,
        "blood_group" : blood_group,
        "ph_number" : ph_number,
        "email" : email,
        "doctor_name" : doctor_name,
        "room": room,
        "location":location,
        "consultation_address" : consultation_address,
        "licence_number" : licence_number,
        "aadhar": aadhar
        }


        collection_di.insert_one(data)

        return jsonify(message="Details Saved successfully!")
    else:
        date = appointment_data['DOB']
        date_object = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_object.strftime('%d-%m-%Y')
        dob_date = datetime.strptime(formatted_date, '%d-%m-%Y')
        current_date = datetime.now()
        agek = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))

        DOB = str(formatted_date)
        age = agek
        address = appointment_data['address']
        blood_group = appointment_data['bloodgroup']
        ph_number = appointment_data['contactnumber']
        doctor_name = appointment_data['name']
        room = appointment_data['consultancyroomnumber']
        location = appointment_data['consultancylocation']
        consultation_address = appointment_data['consultancyaddress']
        licence_number = appointment_data['licence']
        aadhar = appointment_data['aadhar']


        query = {'doctor_username' : main_doctorusername}
        newquery = {"$set" : {
        "DOB" : DOB,
        "age" : age,
        "address" : address,
        "blood_group" : blood_group,
        "ph_number" : ph_number,
        "doctor_name" : doctor_name,
        "room": room,
        "location":location,
        "consultation_address" : consultation_address,
        "licence_number" : licence_number,
        "aadhar": aadhar
        }} 

        collection_di.update_one(query, newquery)

        return jsonify(message="Data Updated successfully!")

@app.route('/accountinfo', methods=['POST', 'GET'])
def accountinfo():
    data = collection_pi.find_one({'patient_username': main_patientusername})
    if data:
        DOBK = data['DOB']
        DOB = datetime.strptime(DOBK, '%d-%m-%Y').strftime('%Y-%m-%d')
        address = data['address']
        blood_group = data['blood_group']
        ph_number = data['ph_number']
        patient_name = data['patient_name']

    return render_template('accountinfo.html', DOB = DOB, address = address, blood_group = blood_group, ph_number = ph_number, patient_name = patient_name)

@app.route('/docaccountinfo', methods=['POST', 'GET'])
def docaccountinfo():
    data = collection_di.find_one({'doctor_username': main_doctorusername})
    if data:
        DOBK = data['DOB']
        DOB = datetime.strptime(DOBK, '%d-%m-%Y').strftime('%Y-%m-%d')
        address = data['address']
        blood_group = data['blood_group']
        ph_number = data['ph_number']
        doctor_name = data['doctor_name']
        aadhar = data['aadhar']
        licence_number = data['licence_number']
        consultation_address = data['consultation_address']
        location = data['location']
        room = data['room']

        print(DOB)
        print(doctor_name)
        print(aadhar)

    return render_template('docaccountinfo.html', DOB = DOB, address = address, blood_group = blood_group, ph_number = ph_number, doctor_name = doctor_name, aadhar = aadhar, licence_number = licence_number, consultation_address = consultation_address, location = location, room = room)


if __name__ == "__main__":
    app.run(debug=True)
