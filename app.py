from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse, Message
import os
import gnupg

from flask import Flask, request
app = Flask(__name__)

load_dotenv()

client = Client(os.environ.get('ACCOUNT_ID'), os.environ.get('AUTH_TOKEN'))

gpg = gnupg.GPG()

@app.route('/')
def index():
    return 'It works!'

@app.route('/sms', methods=['POST'])
def sms():
    body = request.values.get('Body', None)
    from_ = request.values.get('From', None)

    response = MessagingResponse()
    if from_ != os.environ.get('MY_PHONE'):
        response.message('Unauthorized')
        return str(response)

    try:
        with open(os.environ.get('PASS_PATH'), 'rb') as f:
            r = f.read()
            data = str(gpg.decrypt(r, passphrase=os.environ.get('PASSPHRASE')))
            lines = data.split("\n")
            for idx, line in enumerate(lines):
                if body.lower() in line.lower():
                    response.message("\n".join(lines[idx:idx+4]))
    except Exception as e:
        response.message('Failed with ' + str(e))

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
