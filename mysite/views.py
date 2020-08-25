from django.http import HttpResponse
from django.utils.html import escape
import serial
import datetime

def get_value():

    try:

        ser = serial.Serial('/dev/ttyACM0')

        data = ser.read(10).decode()
        ser.close()

        idx = data.index('.')

        if idx == 0 :
            integer_part = "0"
        else:
            integer_part = data[idx - 1]

        decimal_part = data[idx + 1: idx + 3]

        whole_data = integer_part + "." + decimal_part

        if whole_data[-1] == '.':
            whole_data = whole_data[:-1]

    except:
        whole_data = "Cannot open serial port!"

    return whole_data


def funky(request):

    return HttpResponse("Hello Funky!")

def danger(request) :

    try:
        guess = request.GET['guess']

    except Exception:
        guess = "Not found"

    response = """<html><body>
    <p>Your guess was """ + escape(guess) + """</p>
    </body></html>"""
    return HttpResponse(response)

    
def rest(request, guess) :

    try:
        my_guess = guess

    except Exception:
        my_guess = "Not found"

    response = """<html><body>
    <p>Your guess was """ + escape(my_guess) + """</p>
    </body></html>"""
    return HttpResponse(response)

def readarduino(request):

    try:

        now = datetime.datetime.now()
        html = "<html><head><title>My Hello Django</title></head><h1>Hello from Jose Cazarin</h1><body>It is now " + str(now) + "<br>Value read from serial port = " + str(get_value()) + " V </body></html>"
        response = html

    except:
        response = "Server Error!"


    return HttpResponse(response)