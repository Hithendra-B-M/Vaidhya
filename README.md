<div align="center">
<image src="https://github.com/k-arthik-r/Vaidhya/assets/111432615/15e13045-27eb-47bd-8d3e-00b7dc9cc64d"/>
</div>

------------------------

<div align="center">
  <a><img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Tkinter-ff0000?style=for-the-badge&logo=python&logoColor=ffdd54" /></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/MongoDB_Atlas-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Huggingface-FF9D00?style=for-the-badge&logo=huggingface-logo"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Llama 2-0467DF?style=for-the-badge&logo=meta&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Mistral AI-000000?style=for-the-badge&logo=mistralai"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/HKUNLP Instructor L-FFFFFF?style=for-the-badge&logo=hkunlp"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Transformer-gold?style=for-the-badge&logo=package&logoColor=black"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Langchain-FBEEE9?style=for-the-badge&logo=ln"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Chroma DB-999999?style=for-the-badge&logo=chroma-logo"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Samantara-FFFFFF?style=for-the-badge&logo=sam"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Innosetup-FAEBD7?style=for-the-badge&logo=innosetup"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/Random Forest-99EDC3?style=for-the-badge&logo=randforest"></a> &nbsp;
  <a><img src="https://custom-icon-badges.demolab.com/badge/SMTP MIME-FBEC5D?style=for-the-badge&logo=server-smtp"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white"></a> &nbsp;
</div>

------------------------


------------------------

## Requirments
Python 3.9.13 (Recommended) 

<a href="https://www.python.org/downloads](https://www.python.org/downloads/release/python-3913/" alt="python">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>

<br>
<br>

Mongo DB Atlas Account(To Save data in cloud) or Mongo DB Compass(To Save the Data Locally)

<a href="https://www.mongodb.com/" alt="mongo">
      <img src="https://img.shields.io/badge/MongoDB_Atlas-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></a>
        
<br>
<br>

App Password from your Google Account(To Connect and Send Mails through MIEME(SMTP))

<a href="https://www.google.co.in/" alt="mongo">
      <img src="https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white"></a>

--------------------

## Modules/Libraries Used

All The Modules/Libraries Used in the Project can be installed using [requirements.txt](requirements.txt)

- Flask
- Pymongo
- requests
- joblib
- smtplib
- pandas
- configparser 
- email.mime.text 
- email.mime.multipart
- docx
- datetime 
- os
- random

--------------------

## Setup

### Database
Use the Database Configuration File to Setup all the Collections with the name given in the Document.
<br>
- Database Name: Vaidhya
- Total Number of Collections: 12

<br>

You can Access the Document [Here](Database_Configurations.pdf)
<br>
Add your Mongo DB Connection String [Here](config.ini)

<br>

### Google App Password
create a google app password for the google account from which other rescive all mails.

- SENDER_EMAIL -> Source Mail Address.
- SENDER_PASSWORD -> App Password Corresponding to the Source Mail Address.
- RECEIVER_EMAIL -> Maild ID which receives responses from contact us section in About Page.

Add all these Data [Here](config.ini)

<br>

### Coloab URLS
Add the Corresponding Chatbot, Translation, Feeing Expressor Endpoints [Here](config.ini)

<br>

### Flask Secret Key
Add a Custom made FLASK APP SECRET KEY [Here](config.ini)

--------------------------
## How to Run?

- Intialize a Git Repository.
  
```bash
  git init
```

- Clone the Current Git Repository.
  
```bash
  git clone https://github.com/k-arthik-r/Vaidhya.git
```

- Crete a Virtual Environment named env and Activate it(PowerShell)
  
```bash
  python -m venv env

  .\env\Scripts\Activate.ps1
```

- Install all the Modules Present in [requirements](requirements.txt)
  
```bash
  pip install -r requirements.txt
```

- Comeplete the Above setup phase and add all the required credentials in [config.ini](config.ini)
  
```bash
  python app.py
```


-------------------------

## Important Notes:
- The Website in currently PC Responsive only, contributers are invited to modify the CSS files to Make it Responsive which will be revived and accepted.
- The Appointment is currently Desined to save appointments only for a specific date irrespective on the Doctor.

-------------------------

## Archetecture

-------------------------

## Working

The Entire Project is Divided into 2 Parts:
- Patient's Interface
- Doctor's Interface

### Patient's Interface

#### Patient Login Page

Features:
- Input fields for username and password to authenticate the patient.
- Links for creating a new account and resetting the password.
- Language selection dropdown to accommodate multiple languages.
- Navigation link to the About Page.

<br>
  
#### Account Management

Create New Account:
- Form to collect user details including name, email, password, and other necessary information.
- Email verification step for account activation.

Reset Password:
- Email-based password reset link or security question-based password reset option.

<br>
  
#### Patient Dashboard

Features:
- Access to the Helpline Chatbot for immediate support and inquiries.
- Disease Prediction section where patients can undergo tests to predict their mental state.
- Feeling Submission section to schedule appointments based on the user's emotional state.
- Display upcoming appointments and recent interactions with doctors.

<br>
  
#### Test Page

Features:
- A set of 10 scenario-based questions to help predict the patient's mental state.
- Immediate feedback or result based on the responses.

<br>
  
#### Feel Page

Features:
- Powered by a Language Model (LLM) to classify and interpret the patient's feelings.
- Predicts the mental state based on the submitted feelings.
- Option to schedule an appointment with a doctor based on the assessment.
  
<br>
<br>

### Doctor's Interface

#### Doctor Login Page

Features:
- Input fields for username and password to authenticate the doctor.
- Links for creating a new account and resetting the password.
- Language selection dropdown to accommodate multiple languages.
- Navigation link to the About Page.

<br>
  
#### Account Management

Create New Account:
- Form to collect user details including name, email, password, licence, and other necessary information.
- Email verification step for account activation.

Reset Password:
- Email-based password reset link or security question-based password reset option.

<br>

#### Doctor Dashboard

Features:
- View and manage patient reports.
- Offer and manage appointments based on predefined slots and custom availability.
- Access to patient interactions and historical data.

<br>

#### Report Page

Features:
- Fetch patient report using patient ID and doctor access key (constructed as: doctor id + first 2 letters of doctor's name in lowercase).
- Download patient reports in a pre-defined template for record-keeping and analysis.

<br>
  
#### Appointment Page

Features:
- Offer appointments in predefined time slots.
- Option to set one custom slot based on the doctor's availability.
- View and manage scheduled appointments.

------------------------------
