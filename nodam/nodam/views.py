from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render
from .models import SignUp

def index(request):
    return render(request,'index.html')

def community(request):
    return render(request,'community.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        userID = request.POST['userID']
        userPW = request.POST['userPW1']
        userName = request.POST['userName']
        userbirthDay = request.POST['userbirthDay']
        userGender = request.POST['userGender']
        userEmail = request.POST['userEmail']
        userPhone = request.POST['userPhone']
        userAttitude = request.POST['userAttitude']
        startDay = request.POST['startDay']

        SignUp.objects.create(userID=userID, userPW=make_password(userPW), userName=userName,
                            userbirthDay=userbirthDay, userEmail=userEmail,userGender=userGender,
                            userPhone=userPhone,userAttitude=userAttitude,startDay=startDay)
        return redirect('/')

def login(request):
    if request.method == 'POST':
        userID = request.POST['username']
        userPW = request.POST['password']
        if userID and userPW: 
            user = SignUp.objects.get(userID=userID)

            if check_password(userPW , user.userPW):
                request.session['username'] = user.userID
                return redirect('/')
            else:
                return redirect('/login')
    else: 
        return render(request,'login.html')

def logout(requests):
    del requests.session['username']
    return redirect('/')