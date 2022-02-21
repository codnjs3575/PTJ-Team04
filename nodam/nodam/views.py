from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect, render
from .models import SignUp, MyBoard
from django.utils import timezone
from django.core.paginator import Paginator
###

def index(requests): return render(requests,'index.html')
def dashboard(requests): return render(requests,'dashboard.html')
def smokingmap(requests): return render(requests,'map.html')
def clinic(requests): return render(requests,'clinic.html')
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

#
#
#
def community(requests):
    myboard = MyBoard.objects.all().order_by('-id')
    paginator = Paginator(myboard, 5)
    page_num = requests.GET.get('page', '1')

    page_obj = paginator.get_page(page_num)

    try:
        print(page_obj.next_page_number())
        print(page_obj.previous_page_number())
    except:
        pass
    print(page_obj.start_index())
    print(page_obj.end_index())

    return render(requests,'community.html', {'list': page_obj})


def insert_form(request):
    return render(request, 'insert.html')


def insert_res(request):
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('/community/')
    else:
        return redirect('insertform')


def detail(request, id):
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

    if result_title + result_content == 2 :
        return redirect('/detail/'+id)
    else :
        return redirect('/updateform/'+id)

def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]:
        return redirect('/community/')
    else:
        return redirect('detail/' + id)