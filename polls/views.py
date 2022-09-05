from multiprocessing import context
from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
import json as js

# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    f = open('sample4.json')
    context = js.load()
    return render(request,"index.html",context['people'])
    f.close() 