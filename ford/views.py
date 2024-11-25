from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mustang(request):
    return HttpResponse('''<h1>FORD MUSTANG 1969 </h1>
    <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFYTgLjrzrrsQRFJsQ-p-S9CrWJmJW-eOEqg&s'> ''')