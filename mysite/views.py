from django.http import HttpResponse
from django.utils.html import escape
import serial
import datetime

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