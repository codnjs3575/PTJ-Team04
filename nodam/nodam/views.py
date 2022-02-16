from django.shortcuts import render

def index(requests):
    return render(requests,'index.html')

def community(requests):
    return render(requests,'community.html')

def signup(requests):
    return render(requests,'signup.html')

def login(requests):
    return render(requests,'login.html')