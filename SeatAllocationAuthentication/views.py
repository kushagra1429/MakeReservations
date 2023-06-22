from django.shortcuts import redirect, render

# from SeatAllocation.views import bookings, BookingsAdmin

# from SeatAllocation.views import bookings, BookingsAdmin

# from SeatAllocationSystem.settings import AUTHENTICATION_BACKENDS
from .models import User
from django.contrib.auth import authenticate,login
from SeatAllocation.views import *

from SeatAllocation.models import *

# from SeatAllocationSystem.backend import *
import requests
import time
from django.contrib import messages
# Create your views here.
from django.contrib.sessions.models import Session

def SignUp(request):
    #AdminCreate
    name_Admin="Gaurang Trivedi"
    EmailAdmin="gaurang.trivedi@adani.com"
    CodeAdmin="30011591"
    Mobile_Admin="8696931710"
    x=User.objects.all()
    user=User.objects.filter(EmployeeEmail=EmailAdmin, Code=CodeAdmin).exists()
    print(user)
    if user is False:
        Enjoyers=User(EmployeeName=name_Admin, EmployeeEmail=EmailAdmin, EmployeeMobile=Mobile_Admin, Code=CodeAdmin)
        Enjoyers.save()
    else:
        pass

    return render(request, "Authentication/SignUp.html")

def Register(request):   
    if request.method=='POST':
        EmployeeName=request.POST['EmployeeName']
        EmployeeEmail=request.POST['EmployeeEmail']
        EmployeeMobile=request.POST['EmployeeMobile']
        Code=request.POST['Code']

        print(EmployeeName)

        user_exist=User.objects.filter(EmployeeName=EmployeeName)
        email_exist=User.objects.filter(EmployeeEmail=EmployeeEmail)
        mobile_exist=User.objects.filter(EmployeeMobile=EmployeeMobile)
        Code_exist=User.objects.filter(Code=Code)

        if user_exist:
            message="User already exists"
            print("User already exists")
            messages.info(request, "User already exists!")
            return redirect(SignUp) 
        elif email_exist:
            message="Email already exists"
            print("Email already exists")
            messages.info(request, "Email already exists!")
            return redirect(SignUp) 
 
        elif mobile_exist:
            message="Mobile Number already exists"
            print("Conact Number  already exists")
            return redirect(SignUp) 
 
        elif Code_exist:
            message="Use the Code assigned to you"
            print("Enter your own code")
            messages.info(request, "Enter your own code!")

            return redirect(SignUp) 

        else:
            Enjoyers=User(EmployeeName=EmployeeName, EmployeeEmail=EmployeeEmail, EmployeeMobile=EmployeeMobile, Code=Code)
            Enjoyers.save()
            print("SignIn to use the web app!")
            messages.info(request, "Account Successfully Created!")
            time.sleep(3)
            return redirect("SignIn")
        
    
def SignIn(request):
    # text=request.session['error_message']
    # print(text)
    # message_display=request.session.get("Msg")
    return render(request, "Authentication/SignIn.html")

def SignInAuthenticate(request):
    if request.method=='POST':
        EmployeeEmail=request.POST['username']
        Code=request.POST['Code']
        print(EmployeeEmail)
        print(Code)
        print(type(Code))
        name_Admin="Gaurang Trivedi"
        EmailAdmin="gaurang.trivedi@adani.com"
        CodeAdmin="30011591"
        Mobile_Admin="8696931710"
        x=User.objects.all()
        user=User.objects.filter(EmployeeEmail=EmployeeEmail, Code=Code).exists()
        print(user)
        userLog=authenticate(username=EmployeeEmail, password=Code)
        print(userLog)
        # NameUserrr=get_id()
        # if (EmployeeEmail==EmailAdmin and Code==CodeAdmin):
        #     print("TrueAd")

        #     request.session['EmployeeName']=name_Admin
        #     request.session['EmployeeMobile']=Mobile_Admin
        #     request.session['Code']=CodeAdmin
        #     time.sleep(1)
        #     login(request, userLog)
        #     return redirect(BookingsAdmin)    

        if user is False:
            messages.error(request, "User does not exists!")
            return redirect(SignIn)
        
        else:   
            auth=User.objects.filter(EmployeeEmail=EmployeeEmail).values()
            # print(auth)
            for x in auth:
                name_user=x['EmployeeName']
                Mobile_user=x['EmployeeMobile']
                code_user=x['Code']

                print(name_user)
                
                request.session['EmployeeName']=name_user
                request.session['EmployeeMobile']=Mobile_user
                request.session['Code']=code_user
            login(request, userLog)
            # if userLog.is_authenticated:
            #     print("True")
            # print(k)
            print("User is llogggeedd")
            if (EmployeeEmail==EmailAdmin):
                print("Admin")
                time.sleep(1)
                return redirect(BookingsAdmin)
            else:
                time.sleep(1)
                return redirect(bookings)
                
# def SignInAdmin(request):
#     if request.method=='POST':
#         EmployeeEmail=request.POST['EmployeeEmail']
#         Code=request.POST['Code']
#         print(EmployeeEmail)
#         print(Code)
        
        
            

       