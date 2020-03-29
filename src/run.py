from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("STOP COVID vp and aman: ")

    print(request.path)
    print(request)


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
