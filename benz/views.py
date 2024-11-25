from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def GWagon(request):
    return HttpResponse('''<h1>G63 AMG</h1>
    <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmP9rreAUOm83Rj6qNEMqhrTR5ImZ1jSqUTQ&s'>''')