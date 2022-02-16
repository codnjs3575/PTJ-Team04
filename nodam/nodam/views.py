from django.shortcuts import render

def index(requests): return render(requests,'index.html')
def signup(requests): return render(requests,'signup.html')
def login(requests): return render(requests,'login.html')
def dashboard(requests): return render(requests,'dashboard.html')
def smokingmap(requests): return render(requests,'map.html')
def clinic(requests): return render(requests,'clinic.html')
def community(requests): return render(requests,'community.html')