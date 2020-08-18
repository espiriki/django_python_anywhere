from django.http import HttpResponse
import serial

def get_value():

    ser = serial.Serial('COM5')

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

    return HttpResponse("Value read from serial port = " + str(get_value()))