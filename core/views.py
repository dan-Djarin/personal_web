from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>My personal web</h1><h2>Cover page</h2>")

