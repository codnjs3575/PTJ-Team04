from django.db import models

class SignUp(models.Model):
    userID = models.CharField(max_length=50, unique=True)
    userPW = models.CharField(max_length=1000)
    userName = models.CharField(max_length=50)
    userbirthDay = models.CharField(max_length=50)
    userGender = models.CharField(max_length=50)
    userEmail = models.EmailField(max_length=50, unique=True)
    userPhone = models.CharField(max_length=50, unique=True)
    userAttitude = models.CharField(max_length=50)
    startDay = models.DateField()


    def __str__(self):
        return str({'userID': self.userID, 'userPW': self.userPW, 'userName':self.userName,
                    'userGender':self.userGender, 'userEmail':self.userEmail, 
                    'userbirthDay':self.userbirthDay,'userPhone':self.userPhone, 'userAttitude':self.userAttitude,
                    'startDay':self.startDay})

    class Meta:
        db_table= 'signup'


class MyBoard(models.Model):   # MyBoard라는 table
    myname = models.CharField(max_length=100)   # column
    mytitle = models.CharField(max_length=500)   # column
    mycontent = models.CharField(max_length=1000)   # column
    mydate = models.DateTimeField()   # column

    def __str__(self):
        return str({'myname': self.myname, 'mytitle':self.mytitle, 'mycontent': self.mycontent, 'mydate':self.mydate })


class MyMember(models.Model):
    myname = models.CharField(max_length=100)
    mypassword = models.CharField(max_length=100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({'myname': self.myname, 'mypassword':self.mypassword, 'myemail': self.myemail})