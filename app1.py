from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)


translate_api_url = 'http://f44e-34-133-112-46.ngrok-free.app/'


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/name', methods=['GET', 'POST'])
def name():
    return render_template('name.html')

# # Define a route for the dashboard.html page
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# Define a route for the translation endpoint
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

if __name__ == '__main__':
    app.run(debug=True)
