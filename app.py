from flask import Flask, request, make_response, render_template
import random
import string


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ussd', methods=['GET', 'POST'])
def ussdSession():

    if request.method == 'GET':
        return render_template('ussd.html')

    sessionId   = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text        = request.values.get("text", None)

    textArray    = text.split("*") if text else text
    userResponse = textArray[-1] if isinstance(textArray, list) else text

    # Screens
    firstMenu  = '''CON Kenya Power

    1. Account information
    2. Buy tokens
    3. Previous monthly Usage
    98. More
    '''
    secondMenu = '''CON Kenya Power

    4. Get monthly bill(s) on email
    5. Disconnection SMS alerts
    6. Report power outages
    7. CustomerCare Centre Numbers
    0. Previous
    '''
    error      = "END Invalid input"

    # Session logic
    if userResponse == 0  or userResponse == '':
        menu = firstMenu
    elif userResponse == '98':
        menu = secondMenu
    #  more logic  here
    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
