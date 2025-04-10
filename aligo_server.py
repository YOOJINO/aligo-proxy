from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_sms():
    try:
        aligo_url = "https://apis.aligo.in/send_mass/"
        data = request.form.to_dict()
        response = requests.post(aligo_url, data=data)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ip', methods=['GET'])
def get_ip():
    ip = requests.get('https://api.ipify.org').text
    return jsonify({"server_ip": ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
