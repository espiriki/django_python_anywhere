from django.http import HttpResponse
import serial
import datetime

def get_value():

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

    return whole_data


def index(request):

    try:

        now = datetime.datetime.now()
        html = "<html><head><title>My Hello Django</title></head><h1>Hello from Jose Cazarin</h1><body>It is now " + str(now) + "<br>Value read from serial port = " + str(get_value()) + " V </body></html>"
        response = html

    except:
        response = "Server Error!"


    return HttpResponse(response)
