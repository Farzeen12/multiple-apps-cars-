from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def M5(request):
    return HttpResponse('''<h1>BMW M5 CS</h1>
    <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHV_7W8G0JVPmTsmejh8UvLlO24Vkf-7jWgA&s'>''')