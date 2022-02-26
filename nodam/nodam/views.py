from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render
from .models import SignUp, MyBoard
from django.utils import timezone
from django.core.paginator import Paginator
###

def index(requests): 
    community = MyBoard.objects.all().order_by('-hit')
    community2 = MyBoard.objects.all().order_by('-mydate')
    if (requests.session.get('username')):
        user_id = requests.session.get('username')
        user = SignUp.objects.get(userID=user_id)
        return render(requests,'index.html',{'userinfo':user, 'community' : community,'community2':community2})
    else :
        return render(requests,'index.html',{'community' : community,'community2':community2})
    
def dashboard(requests): 
    if (requests.session.get('username')):
        user_id = requests.session.get('username')
        user = SignUp.objects.get(userID=user_id)
        return render(requests,'dashboard1.html',{'userinfo':user})
    else :
        return render(requests,'dashboard1.html')
    
    
def smokingmap(requests): 
    if (requests.session.get('username')):
        user_id = requests.session.get('username')
        user = SignUp.objects.get(userID=user_id)
        return render(requests,'map.html',{'userinfo':user})
    else :
        return render(requests,'map.html')

def clinic(requests): 
    if (requests.session.get('username')):
        user_id = requests.session.get('username')
        print(user_id)
        user = SignUp.objects.get(userID=user_id)
        return render(requests,'clinic.html',{'userinfo':user})
    else :
        return render(requests,'clinic.html')
        
def dashboard1(requests): return render(requests,'dashboard1.html')
def dashboard2(requests): return render(requests,'dashboard2.html')
def dashboard3(requests): return render(requests,'dashboard3.html')
def dashboard4(requests): return render(requests,'dashboard4.html')


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
        return redirect('/login')

def login(request):
    # return render(requests,'index.html',{'userinfo':users})
    if request.method == 'POST':
        userID = request.POST['username']
        userPW = request.POST['password']
        

        if userID and userPW: 
            user = SignUp.objects.get(userID=userID)
            
            # if userPW == user.userPW:
            if check_password(userPW , user.userPW):
                print(userPW,user)
                request.session['username'] = user.userID
                # return render(request,'index.html',{'userinfo':user})
                return redirect('/')
            else:
                return redirect('/login')
    else: 
        return render(request,'login.html')

def logout(requests):
    del requests.session['username']
    return redirect('/')

#
#
#
def community(requests):
    myboardCount = MyBoard.objects.count()
    myboard = MyBoard.objects.all().order_by('-id')

    paginator = Paginator(myboard, 10)
    page_num = requests.GET.get('page', '1')

    page_obj = paginator.get_page(page_num)

    return render(requests, 'community.html', {'list': page_obj, "myboard":myboard, "myboardCount":myboardCount})


def insert_form(request):
    return render(request, 'insert.html')


def insert_res(requests):
    myname = requests.session.get('username')
    mytitle = requests.POST['mytitle']
    mycontent = requests.POST['mycontent']

    result = MyBoard.objects.create(myname=myname,mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('/community/')
    else:
        return redirect('insertform')


def detail(request, id):

    # 조회수 증가
    dto = MyBoard.objects.get(id=id)
    dto.hit_up()
    dto.save()

    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def update_form(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)

    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    result_time = myboard.update(mydate=timezone.now())

    if result_title + result_content + result_time == 3 :
        return redirect('/detail/'+id)
    else :
        return redirect('/updateform/'+id)

def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]:
        return redirect('/community/')
    else:
        return redirect('detail/' + id)