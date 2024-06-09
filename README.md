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
- Patient Login Page - Take input username and password to login to the user'a account.
- Patients can Create New Account using the link present in Patient Login Page.
- Patients can reset account password using the link present in Patient Login Page.
- Patient can choose the respective Language.
- Patient can Navigate to the About Page.
  
#### Patient Dashboard
- where patients have access to Helpline Chatbot, Disease Prediction through Tests and Felling Submission to Schedule an Appointment with the Doctor in the available time slot.

#### Test Page
- where the users are given 10 scenario based question to predict their mental state.
  
#### Feel Page
- powered by LLM, capable of classifiying the given feelings and predict the mental state.

<br><br>

### Doctors's Interface  

#### Doctor Login Page
- Doctor Login Page - Take input username and password to login to the user'a account.
- Doctors can Create New Account using the link present in Patient Login Page.
- Doctors can reset account password using the link present in Patient Login Page.
- Doctors can choose the respective Language.
- Doctors can Navigate to the About Page.
  
#### Patient Dashboard
- can check patient report or offer Appointments based on predefined slots.

#### Report Page
- Fetch Patient Report for the given patient ID and Doctor Access Key. (Key is be doctor id + First 2 letters from doctor name - all lowercase characters)
- Able to download Patient Report in a pre-defined Template
  
#### Appointment Page
- Doctors are provided the privilage of offering the appointments on a predefined slots that are optional. apart from this doctor can also choose one custom slot based on their availability.

------------------------------
