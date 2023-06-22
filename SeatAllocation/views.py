import datetime
import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
# from SeatAllocationAuthentication.views import *
from django.contrib.auth.decorators import login_required
import pandas as pd
import openpyxl
import xlwt

# from . models import 
# from .forms import DateInputBook
from .models import *
import time


# Create your views here.

def download(request):
    x=Monday.objects.all()
    w=Tuesday.objects.all()
    e=Wednessday.objects.all()
    r=Thursday.objects.all()
    t=Friday.objects.all()
    u=Saturday.objects.all()
    o=Sunday.objects.all()
    g=[]
    h=[]
    j=[]
    cf=[]
    jk=[]
    kl=[]
    lm=[]
    NameM=[]
    CodeM=[]
    DateM=[]
    CodeM=[]
    SeatM=[]
    TripM=[]
    DayM=[]
    TimeM=[]
    PurposeM=[]
    MobileM=[]

    maindata={"Monday": g, "Tuesday": h, "Wednessday": j, "Thursday": cf, "Friday": jk, "Saturday": kl, "Sunday": lm}

    for i in range(len(x)):
        name1=Monday.objects.all()[i].EmployeeName
        Seats=Monday.objects.all()[i].BookedSeats
        Mobile_Number=Monday.objects.all()[i].EmployeeMobile

        Code=Monday.objects.all()[i].Code
        trip=Monday.objects.all()[i].Trip
        times=Monday.objects.all()[i].Time
        purpose=Monday.objects.all()[i].Purpose
        Date=Monday.objects.all()[i].Date
        data={"Day": "Monday", "Name": name1, "Code": Code, "Seats": Seats, "trip": trip, "time": times, "purpose": purpose, "date": Date,"MobileNumber": Mobile_Number}

        g.append(data)

    for i in range(len(w)):
        name2=Tuesday.objects.all()[i].EmployeeName
        Mobile_Number2=Tuesday.objects.all()[i].EmployeeMobile

        Seats2=Tuesday.objects.all()[i].BookedSeats
        Code2=Tuesday.objects.all()[i].Code
        trip2=Tuesday.objects.all()[i].Trip
        time2=Tuesday.objects.all()[i].Time
        purpose2=Tuesday.objects.all()[i].Purpose
        Date2=Tuesday.objects.all()[i].Date

        data2={"Day": "Tuesday", "Name": name2,"Code": Code2, "Seats": Seats2, "trip": trip2, "time": time2, "purpose": purpose2, "date": Date2, "MobileNumber": Mobile_Number2}
        h.append(data2)

       
    for i in range(len(e)):
        name3=Wednessday.objects.all()[i].EmployeeName
        Seats3=Wednessday.objects.all()[i].BookedSeats
        Mobile_Number3=Wednessday.objects.all()[i].EmployeeMobile

        Code3=Wednessday.objects.all()[i].Code

        trip3=Wednessday.objects.all()[i].Trip
        time3=Wednessday.objects.all()[i].Time
        purpose3=Wednessday.objects.all()[i].Purpose
        Date3=Wednessday.objects.all()[i].Date

        data3={"Day": "Wednessday", "Name": name3, "Code": Code3,"Seats": Seats3, "trip": trip3, "time": time3, "purpose": purpose3, "date": Date3, "MobileNumber": Mobile_Number3}
        j.append(data3)


    for i in range(len(r)):

        name4=Thursday.objects.all()[i].EmployeeName
        Mobile_Number4=Thursday.objects.all()[i].EmployeeMobile

        Seats4=Thursday.objects.all()[i].BookedSeats
        Code4=Thursday.objects.all()[i].Code

        trip4=Thursday.objects.all()[i].Trip
        time4=Thursday.objects.all()[i].Time
        purpose4=Thursday.objects.all()[i].Purpose
        Date4=Thursday.objects.all()[i].Date

        data4={"Day": "Thursday", "Name": name4,"Code": Code4, "Seats": Seats4, "trip": trip4, "time": time4, "purpose": purpose4, "date": Date4, "MobileNumber": Mobile_Number4}
        cf.append(data4)


    for i in range(len(t)):

        name5=Friday.objects.all()[i].EmployeeName
        Mobile_Number5=Friday.objects.all()[i].EmployeeMobile

        Seats5=Friday.objects.all()[i].BookedSeats
        Code5=Thursday.objects.all()[i].Code

        trip5=Friday.objects.all()[i].Trip
        time5=Friday.objects.all()[i].Time
        purpose5=Friday.objects.all()[i].Purpose
        Date5=Friday.objects.all()[i].Date

        data5={"Day": "Friday" ,"Name": name5, "Code": Code5, "Seats": Seats5, "trip": trip5, "time": time5, "purpose": purpose5, "date": Date5, "MobileNumber": Mobile_Number5}
        jk.append(data5)


    for i in range(len(u)):
        name6=Saturday.objects.all()[i].EmployeeName
        Seats6=Saturday.objects.all()[i].BookedSeats
        Mobile_Number6=Saturday.objects.all()[i].EmployeeMobile

        Code6=Thursday.objects.all()[i].Code

        trip6=Saturday.objects.all()[i].Trip
        time6=Saturday.objects.all()[i].Time
        purpose6=Saturday.objects.all()[i].Purpose
        Date6=Saturday.objects.all()[i].Date

        data6={"Day": "Saturday",  "Name": name6,"Code": Code6, "Seats": Seats6, "trip": trip6, "time": time6, "purpose": purpose6, "date": Date6, "MobileNumber": Mobile_Number6}
        kl.append(data6)


    for i in range(len(o)):
        name7=Sunday.objects.all()[i].EmployeeName
        Seats7=Sunday.objects.all()[i].BookedSeats
        Mobile_Number7=Sunday.objects.all()[i].EmployeeMobile

        Code7=Thursday.objects.all()[i].Code

        trip7=Sunday.objects.all()[i].Trip
        time7=Sunday.objects.all()[i].Time
        purpose7=Sunday.objects.all()[i].Purpose
        Date7=Sunday.objects.all()[i].Date

        data7={"Day": "Sunday", "Name": name7,"Code": Code7, "Seats": Seats7, "trip": trip7, "time": time7, "purpose": purpose7, "date": Date7, "Mobile Number": Mobile_Number7}
        lm.append(data7)

    guv=maindata["Monday"]
    for asgh in range(len(guv)):
        g=guv[asgh]
        b=g['Day']
        d=g['Name']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']

        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        TimeM.append(l)
        PurposeM.append(w)
        DateM.append(dt)
        MobileM.append(ll)
    
    tuv=maindata["Tuesday"]
    print(len(tuv))
    for asgh in range(len(tuv)):
        g=tuv[asgh]
        d=g['Name']
        b=g['Day']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']

        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        TimeM.append(l)
        PurposeM.append(w)
        DateM.append(dt)
        MobileM.append(ll)

    uuv=maindata["Wednessday"]
    print(len(uuv))
    for asgh in range(len(uuv)):
        g=uuv[asgh]
        d=g['Name']
        b=g['Day']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']

        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        TimeM.append(l)
        PurposeM.append(w)
        DateM.append(dt)
    ouv=maindata["Thursday"]
    print(len(ouv))
    for asgh in range(len(ouv)):
        g=ouv[asgh]
        d=g['Name']
        b=g['Day']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']

        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        TimeM.append(l)
        PurposeM.append(w)
        MobileM.append(ll)

        DateM.append(dt)
    truv=maindata["Friday"]
    print(len(truv))
    for asgh in range(len(truv)):
        g=truv[asgh]
        d=g['Name']
        b=g['Day']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']

        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        TimeM.append(l)
        PurposeM.append(w)
        MobileM.append(ll)

        DateM.append(dt)
    tfuv=maindata["Saturday"]
    print(len(tfuv))
    for asgh in range(len(tfuv)):
        g=tfuv[asgh]
        d=g['Name']
        b=g['Day']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']

        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        MobileM.append(ll)

        TimeM.append(l)
        PurposeM.append(w)
        DateM.append(dt)
    tufv=maindata["Sunday"]
    print(len(tufv))
    for asgh in range(len(tufv)):
        g=tufv[asgh]
        d=g['Name']
        b=g['Day']
        dt=g['date']
        f=g['Code']
        h=g['Seats']
        k=g['trip']
        l=g['time']
        w=g['purpose']
        ll=g['Mobile Number']
        DayM.append(b)
        NameM.append(d)
        CodeM.append(f)
        SeatM.append(h)
        TripM.append(k)
        TimeM.append(l)
        MobileM.append(ll)

        PurposeM.append(w)
        DateM.append(dt)
    c={"Name": NameM, "Code": CodeM, "Trip": TripM, "Time": TimeM, "Day": DayM, "Date": DateM, "Purpose": PurposeM, "Seats": SeatM, "Mobile Number": MobileM}
    vb=pd.DataFrame(c)
    print(vb)
    # vb.to_excel("Reservations.xlsx", index=False)

    response = HttpResponse(content_type='application/xlsx')
    response['Content-Disposition'] = f'attachment; filename="Reservations.xlsx"'
    with pd.ExcelWriter(response) as writer:
        vb.to_excel(writer, sheet_name='Reservations', index=False)

    # response=HttpResponse(content_type='application/ms-ecxel')
    # response['Content-Disposition']='attachment; filename=Expenses'+ \
    #     str(datetime.datetime.now())+'.xls'
    # wb=xlwt.Workbook(encoding='utf-8')
    # ws=wb.add_sheet('Reservations')
    # row_num=0
    # font_style=xlwt.XFStyle()
    # font_style.font.bold=True
    # columns=['Name', 'Code', 'Trip', 'Time', 'Day', 'Date', 'Purpose', 'Seats']
    # fg=[NameM, CodeM, TripM, TimeM, DayM, DateM, PurposeM, SeatM]
    # for col in range(len(columns)):
    #     ws.write(row_num, col, columns[col], font_style)
    # font_style=xlwt.XFStyle()
    # for row in fg:
    #     row_num+=1
    #     for col in range(len(row)):
    #         ws.write(row_num, col, columns[col], font_style)

    # wb.save(response)
    return response

def DeleteAction(request):
    if request.method=="POST":
        trip=request.POST['trip']
        day=request.POST['Day']
        date=request.POST['Date']
        Time=request.POST['Time']
        Purpose=request.POST['Purpose']
        Seats=request.POST['Seats']
        print(trip, day, date, Time, Purpose, Seats)
        name_user=request.session['EmployeeName'] 
        x=Monday.objects.all()
        w=Tuesday.objects.all()
        e=Wednessday.objects.all()
        r=Thursday.objects.all()
        t=Friday.objects.all()
        u=Saturday.objects.all()
        o=Sunday.objects.all()
        if (day=="Monday"):
            typ=Monday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            messages.info(request, "Your Booking has been cancelled!")
            print(canBook)
            # request.session['Cancel']=canBook
        elif (day=="Tuesday"):
            typ=Tuesday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            print(canBook)
            messages.info(request, "Your Booking has been cancelled!")

            # request.session['Cancel']=canBook
        elif (day=="Wednessday"):
            typ=Wednessday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            print(canBook)
            messages.info(request, "Your Booking has been cancelled!")

            # request.session['Cancel']=canBook
        elif (day=="Thursday"):
            typ=Thursday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            print(canBook)
            messages.info(request, "Your Booking has been cancelled!")

            # request.session['Cancel']=canBook
        elif (day=="Friday"):
            typ=Friday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            print(canBook)
            messages.info(request, "Your Booking has been cancelled!")

            # request.session['Cancel']=canBook
        elif (day=="Saturday"):
            typ=Saturday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            print(canBook)
            messages.info(request, "Your Booking has been cancelled!")

            # request.session['Cancel']=canBook
        elif (day=="Sunday"):
            typ=Sunday.objects.filter(Day=day, Trip=trip, Time=Time, Purpose=Purpose,
                                  BookedSeats=Seats, EmployeeName=name_user).delete()
            canBook="Your Booking has been cancelled!"
            print(canBook)
            messages.info(request, "Your Booking has been cancelled!")

            # request.session['Cancel']=canBook
        time.sleep(1)
        return redirect(MyBookings)


def MyBookings(request):
    name_user=request.session['EmployeeName'] 
    # CanBook=request.session.get('Cancel', False)
    x=Monday.objects.all()
    w=Tuesday.objects.all()
    e=Wednessday.objects.all()
    r=Thursday.objects.all()
    t=Friday.objects.all()
    u=Saturday.objects.all()
    o=Sunday.objects.all()
    g=[]
    h=[]
    j=[]
    cf=[]
    jk=[]
    kl=[]
    lm=[]

    maindata={"Monday": g, "Tuesday": h, "Wednessday": j, "Thursday": cf, "Friday": jk, "Saturday": kl, "Sunday": lm}

    for i in range(len(x)):
        # y=Monday.objects.all()[i]
        # name=Monday.objects.all()[i].EmployeeName
        # Number_of_Seats1=Monday.objects.all()[i].NumberOfSeats
        Name=Monday.objects.all()[i].EmployeeName
        
        if (Name==name_user):
            Seats=Monday.objects.all()[i].BookedSeats
            Code=Monday.objects.all()[i].Code
            trip=Monday.objects.all()[i].Trip
            times=Monday.objects.all()[i].Time
            purpose=Monday.objects.all()[i].Purpose
            Date=Monday.objects.all()[i].Date

            data={"Day": "Monday", "Code": Code, "Seats": Seats, "trip": trip, "time": times, "purpose": purpose, "date": Date}
            g.append(data)


    for i in range(len(w)):
        # Number_of_Seats2=Tuesday.objects.all()[i].NumberOfSeats
        Name2=Tuesday.objects.all()[i].EmployeeName

        if (Name2==name_user):

            Seats2=Tuesday.objects.all()[i].BookedSeats
            Code2=Tuesday.objects.all()[i].Code

            trip2=Tuesday.objects.all()[i].Trip
            time2=Tuesday.objects.all()[i].Time
            purpose2=Tuesday.objects.all()[i].Purpose
            Date2=Tuesday.objects.all()[i].Date

            data2={"Day": "Tuesday", "Code": Code2, "Seats": Seats2, "trip": trip2, "time": time2, "purpose": purpose2, "date": Date2}
            h.append(data2)

       
    for i in range(len(e)):
        Name3=Wednessday.objects.all()[i].EmployeeName
        if (Name3==name_user):

            Seats3=Wednessday.objects.all()[i].BookedSeats
            Code3=Wednessday.objects.all()[i].Code

            trip3=Wednessday.objects.all()[i].Trip
            time3=Wednessday.objects.all()[i].Time
            purpose3=Wednessday.objects.all()[i].Purpose
            Date3=Wednessday.objects.all()[i].Date

            data3={"Day": "Wednessday", "Code": Code3,"Seats": Seats3, "trip": trip3, "time": time3, "purpose": purpose3, "date": Date3}
            j.append(data3)


    for i in range(len(r)):

        Name4=Thursday.objects.all()[i].EmployeeName
        if (Name4==name_user):
            Seats4=Thursday.objects.all()[i].BookedSeats
            Code4=Thursday.objects.all()[i].Code
            trip4=Thursday.objects.all()[i].Trip
            time4=Thursday.objects.all()[i].Time
            purpose4=Thursday.objects.all()[i].Purpose
            Date4=Thursday.objects.all()[i].Date

            data4={"Day": "Thursday", "Code": Code4, "Seats": Seats4, "trip": trip4, "time": time4, "purpose": purpose4, "date": Date4}
            cf.append(data4)


    for i in range(len(t)):

        Name5=Friday.objects.all()[i].EmployeeName
        if (Name5==name_user):

            Seats5=Friday.objects.all()[i].BookedSeats
            Code5=Friday.objects.all()[i].Code

            trip5=Friday.objects.all()[i].Trip
            time5=Friday.objects.all()[i].Time
            purpose5=Friday.objects.all()[i].Purpose
            Date5=Friday.objects.all()[i].Date

            data5={"Day": "Friday", "Code": Code5, "Seats": Seats5, "trip": trip5, "time": time5, "purpose": purpose5, "date": Date5}
            jk.append(data5)


    for i in range(len(u)):
        Name6=Saturday.objects.all()[i].EmployeeName
        if (Name6==name_user):

            Seats6=Saturday.objects.all()[i].BookedSeats
            Code6=Saturday.objects.all()[i].Code

            trip6=Saturday.objects.all()[i].Trip
            time6=Saturday.objects.all()[i].Time
            purpose6=Saturday.objects.all()[i].Purpose
            Date6=Saturday.objects.all()[i].Date

            data6={"Day": "Saturday", "Code": Code6, "Seats": Seats6, "trip": trip6, "time": time6, "purpose": purpose6, "date": Date6}
            kl.append(data6)


    for i in range(len(o)):
        Name7=Sunday.objects.all()[i].EmployeeName
        if (Name7==name_user):

            Seats7=Sunday.objects.all()[i].BookedSeats
            Code7=Sunday.objects.all()[i].Code

            trip7=Sunday.objects.all()[i].Trip
            time7=Sunday.objects.all()[i].Time
            purpose7=Sunday.objects.all()[i].Purpose
            Date7=Sunday.objects.all()[i].Date

            data7={"Day": "Sunday", "Code": Code7, "Seats": Seats7, "trip": trip7, "time": time7, "purpose": purpose7, "date": Date7}
            lm.append(data7)

    # print(maindata)
    Details={"name_user": name_user, "data": maindata}
    # print(Details)
    details=json.dumps(Details)

    time.sleep(1)
    return render(request, "SeatAllocation/MyBookings.html", {"user": details})


def MyBookingsAdmin(request):
    name_user=request.session['EmployeeName'] 
    # CanBook=request.session.get('Cancel', False)
    x=Monday.objects.all()
    w=Tuesday.objects.all()
    e=Wednessday.objects.all()
    r=Thursday.objects.all()
    t=Friday.objects.all()
    u=Saturday.objects.all()
    o=Sunday.objects.all()
    g=[]
    h=[]
    j=[]
    cf=[]
    jk=[]
    kl=[]
    lm=[]

    maindata={"Monday": g, "Tuesday": h, "Wednessday": j, "Thursday": cf, "Friday": jk, "Saturday": kl, "Sunday": lm}

    for i in range(len(x)):
        # y=Monday.objects.all()[i]
        # name=Monday.objects.all()[i].EmployeeName
        # Number_of_Seats1=Monday.objects.all()[i].NumberOfSeats
        Name=Monday.objects.all()[i].EmployeeName
        if (Name==name_user):
            Seats=Monday.objects.all()[i].BookedSeats
            Code=Monday.objects.all()[i].Code
            trip=Monday.objects.all()[i].Trip
            times=Monday.objects.all()[i].Time
            purpose=Monday.objects.all()[i].Purpose
            Date=Monday.objects.all()[i].Date

            data={"Day": "Monday", "Code": Code, "Seats": Seats, "trip": trip, "time": times, "purpose": purpose, "date": Date}
            g.append(data)


    for i in range(len(w)):
        # Number_of_Seats2=Tuesday.objects.all()[i].NumberOfSeats
        Name2=Tuesday.objects.all()[i].EmployeeName

        if (Name2==name_user):
            Seats2=Tuesday.objects.all()[i].BookedSeats
            Code2=Tuesday.objects.all()[i].Code

            trip2=Tuesday.objects.all()[i].Trip
            time2=Tuesday.objects.all()[i].Time
            purpose2=Tuesday.objects.all()[i].Purpose
            Date2=Tuesday.objects.all()[i].Date

            data2={"Day": "Tuesday", "Code": Code2, "Seats": Seats2, "trip": trip2, "time": time2, "purpose": purpose2, "date": Date2}
            h.append(data2)

       
    for i in range(len(e)):
        Name3=Wednessday.objects.all()[i].EmployeeName
        if (Name3==name_user):
            Seats3=Wednessday.objects.all()[i].BookedSeats
            Code3=Wednessday.objects.all()[i].Code

            trip3=Wednessday.objects.all()[i].Trip
            time3=Wednessday.objects.all()[i].Time
            purpose3=Wednessday.objects.all()[i].Purpose
            Date3=Wednessday.objects.all()[i].Date

            data3={"Day": "Wednessday", "Code": Code3,"Seats": Seats3, "trip": trip3, "time": time3, "purpose": purpose3, "date": Date3}
            j.append(data3)


    for i in range(len(r)):

        Name4=Thursday.objects.all()[i].EmployeeName
        if (Name4==name_user):
            Seats4=Thursday.objects.all()[i].BookedSeats
            Code4=Thursday.objects.all()[i].Code

            trip4=Thursday.objects.all()[i].Trip
            time4=Thursday.objects.all()[i].Time
            purpose4=Thursday.objects.all()[i].Purpose
            Date4=Thursday.objects.all()[i].Date

            data4={"Day": "Thursday", "Code": Code4, "Seats": Seats4, "trip": trip4, "time": time4, "purpose": purpose4, "date": Date4}
            cf.append(data4)


    for i in range(len(t)):

        Name5=Friday.objects.all()[i].EmployeeName
        if (Name5==name_user):
            Seats5=Friday.objects.all()[i].BookedSeats
            Code5=Thursday.objects.all()[i].Code

            trip5=Friday.objects.all()[i].Trip
            time5=Friday.objects.all()[i].Time
            purpose5=Friday.objects.all()[i].Purpose
            Date5=Friday.objects.all()[i].Date

            data5={"Day": "Friday", "Code": Code5, "Seats": Seats5, "trip": trip5, "time": time5, "purpose": purpose5, "date": Date5}
            jk.append(data5)


    for i in range(len(u)):
        Name6=Saturday.objects.all()[i].EmployeeName
        if (Name6==name_user):
            Seats6=Saturday.objects.all()[i].BookedSeats
            Code6=Thursday.objects.all()[i].Code

            trip6=Saturday.objects.all()[i].Trip
            time6=Saturday.objects.all()[i].Time
            purpose6=Saturday.objects.all()[i].Purpose
            Date6=Saturday.objects.all()[i].Date

            data6={"Day": "Saturday", "Code": Code6, "Seats": Seats6, "trip": trip6, "time": time6, "purpose": purpose6, "date": Date6}
            kl.append(data6)


    for i in range(len(o)):
        Name7=Sunday.objects.all()[i].EmployeeName
        if (Name7==name_user):
            Seats7=Sunday.objects.all()[i].BookedSeats
            Code7=Thursday.objects.all()[i].Code

            trip7=Sunday.objects.all()[i].Trip
            time7=Sunday.objects.all()[i].Time
            purpose7=Sunday.objects.all()[i].Purpose
            Date7=Sunday.objects.all()[i].Date

            data7={"Day": "Sunday", "Code": Code7, "Seats": Seats7, "trip": trip7, "time": time7, "purpose": purpose7, "date": Date7}
            lm.append(data7)

    # print(maindata)
    Details={"name_user": name_user, "data": maindata}
    # print(Details)
    details=json.dumps(Details)

    time.sleep(1)
    return render(request, "SeatAllocation/MyBookings.html", {"user": details})


def Authenticate(request):
    if request.method=="POST":
        Day=request.POST['Day']
        Trip=request.POST['Trip']
        Time=request.POST['Time']
        Purpose=request.POST['Purpose']
        Date=request.POST['Date']
        BookedSeats=request.POST.get('BookedSeats')
        NumberOfSeat=request.POST.get('NumberOfSeats')
        EmployeeName=request.POST['EmployeeName']
        EmployeeMobile=request.POST['EmployeeMobile']
        Code=request.POST['Code']
        
        if Day=="Monday":
            Customers=Monday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            # confirm="Your Booking is confirmed"
            # request.session["Your Booking is confirmed"]
            # print(Confirm)
            return redirect(bookings)

        elif Day=="Tuesday":
            Customers=Tuesday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            confirm="Your Booking is confirmed"
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            # print(Confirm)
            return redirect(bookings)

        elif Day=="Wednessday":
            Customers=Wednessday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            confirm="Your Booking is confirmed"
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            return redirect(bookings)
        
        elif Day=="Thursday":
            Customers=Thursday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            confirm="Your Booking is confirmed"
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            return redirect(bookings)
        
        elif Day=="Friday":
            Customers=Friday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            confirm="Your Booking is confirmed"
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            return redirect(bookings)
        
        elif Day=="Saturday":
            Customers=Saturday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            confirm="Your Booking is confirmed"
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            return redirect(bookings)
        
        elif Day=="Sunday":
            Customers=Sunday(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
            # messages.success(request, "User Saved")
            Customers.save()
            confirm="Your Booking is confirmed"
            time.sleep(1)
            messages.info(request, "Your Booking has been confirmed")
            return redirect(bookings)

        else:
            return redirect(bookings)
        
        # Customers=User(Day=Day, Trip=Trip, Time=Time, Purpose=Purpose, Date=Date, BookedSeats=BookedSeats, NumberOfSeats=NumberOfSeat, EmployeeName=EmployeeName, EmployeeMobile=EmployeeMobile, Code=Code)
        # messages.success(request, "User Saved")
        # Customers.save()

        # Users=User.objects.create_user(EmployeeName, EmployeeMobile, Code)
        # Users.save()
        # messages.success(request, 'User Saved')

        # return render(request, "SeatAllocation/bookings.html", {"message": confirm}) 
    

# @login_required
def bookings(request):
    x=Monday.objects.all()
    w=Tuesday.objects.all()
    e=Wednessday.objects.all()
    r=Thursday.objects.all()
    t=Friday.objects.all()
    u=Saturday.objects.all()
    o=Sunday.objects.all()
    SeatAndDate=[]
    SeatAndDate2A=[]
    SeatAndDate2B=[]
    SeatAndDate2=[]
    SeatAndDate3A=[]
    SeatAndDate3=[]
    SeatAndDate4A=[]
    SeatAndDate4B=[]
    SeatAndDate4=[]
    SeatAndDate5A=[]
    SeatAndDate5B=[]
    SeatAndDate5=[]
    SeatAndDate6A=[]
    SeatAndDate6=[]
    SeatAndDate7A=[]
    SeatAndDate7=[]


    day={"BookedSeats1": SeatAndDate, "BookedSeats2A": SeatAndDate2A, "BookedSeats2B": SeatAndDate2B,
         "BookedSeats2": SeatAndDate2, "BookedSeats3A": SeatAndDate3A, "BookedSeats3": SeatAndDate3, "BookedSeats4A": SeatAndDate4A, "BookedSeats4B": SeatAndDate4B
         ,"BookedSeats4": SeatAndDate4, "BookedSeats5A": SeatAndDate5A, "BookedSeats5B": SeatAndDate5B, "BookedSeats5": SeatAndDate5, 
         "BookedSeats6A": SeatAndDate6A, "BookedSeats6": SeatAndDate6, "BookedSeats7A": SeatAndDate7A, "BookedSeats7": SeatAndDate7}
    
    

    for i in range(len(x)):
        Seats1=Monday.objects.all()[i].BookedSeats
        Date1=Monday.objects.all()[i].Date
        p={"Seats": Seats1, "date": Date1}
        SeatAndDate.append(p)

    for i in range(len(w)):
        # Number_of_Seats2=Tuesday.objects.all()[i].NumberOfSeats
        Trip=Tuesday.objects.all()[i].Trip
        Time=Tuesday.objects.all()[i].Time
        

        # print(Trip)
        if (Trip=="Kota Station to Township"):
            if (Time=="8:00AM"):
                Seats2A=Tuesday.objects.all()[i].BookedSeats
                Date2A=Tuesday.objects.all()[i].Date
                p={"Seats": Seats2A, "date": Date2A}
                SeatAndDate2A.append(p)
            elif (Time=="8:30PM"):
                Seats2B=Tuesday.objects.all()[i].BookedSeats
                Date2B=Tuesday.objects.all()[i].Date
                p={"Seats": Seats2B, "date": Date2B}
                SeatAndDate2B.append(p)
            elif (Trip=="Township to Kota Station"):
                Seats2=Tuesday.objects.all()[i].BookedSeats
                Date2=Tuesday.objects.all()[i].Date
                p={"Seats": Seats2, "date": Date2}
                SeatAndDate2.append(p)
        # day["Number2"].append(Number_of_Seats2)
       
    for i in range(len(e)):
        # Number_of_Seats3=Monday.objects.all()[i].NumberOfSeats
        Trip=Wednessday.objects.all()[i].Trip
        
        if (Trip=="Township to Kota Station"):
            Seats3A=Wednessday.objects.all()[i].BookedSeats
            Date3A=Wednessday.objects.all()[i].Date
            p={"Seats": Seats3A, "date": Date3A}
            SeatAndDate3A.append(p)
        elif (Trip=="Kota Station to Township"):
            Seats3=Wednessday.objects.all()[i].BookedSeats
            Date3=Wednessday.objects.all()[i].Date
            p={"Seats": Seats3, "date": Date3}
            SeatAndDate3.append(p)
        # day["Number3"].append(Number_of_Seats3)

    for i in range(len(r)):
        Trip=Thursday.objects.all()[i].Trip

        # Number_of_Seats4=Thursday.objects.all()[i].NumberOfSeats
        if (Trip=="Township to Kota Station"):
            Seats4=Thursday.objects.all()[i].BookedSeats
            Date4=Thursday.objects.all()[i].Date
            p={"Seats": Seats4, "date": Date4}
            SeatAndDate4.append(p)
        elif (Trip=="Township to Baran"):
            Seats4A=Thursday.objects.all()[i].BookedSeats
            Date4A=Thursday.objects.all()[i].Date
            p={"Seats": Seats4A, "date": Date4A}
            SeatAndDate4A.append(p)
        elif (Trip=="Baran to Township"):
            Seats4B=Thursday.objects.all()[i].BookedSeats
            Date4B=Thursday.objects.all()[i].Date
            p={"Seats": Seats4B, "date": Date4B}
            SeatAndDate4B.append(p)
        # day["Number4"].append(Number_of_Seats4)

    for i in range(len(t)):
        Trip=Friday.objects.all()[i].Trip
        Time=Friday.objects.all()[i].Time
        # print(Trip)
        if (Trip=="Kota Station to Township"):
            if (Time=="8:00AM"):
                Seats5A=Friday.objects.all()[i].BookedSeats
                Date5A=Friday.objects.all()[i].Date
                p={"Seats": Seats5A, "date": Date5A}
                SeatAndDate5A.append(p)
            elif (Time=="8:30PM"):
                Seats5B=Friday.objects.all()[i].BookedSeats
                Date5B=Friday.objects.all()[i].Date
                p={"Seats": Seats5B, "date": Date5B}
                SeatAndDate5B.append(p)
        elif (Trip=="Township to Kota Station"):
            # Number_of_Seats5=Friday.objects.all()[i].NumberOfSeats
            Seats5=Friday.objects.all()[i].BookedSeats
            Date5=Friday.objects.all()[i].Date
            p={"Seats": Seats5, "date": Date5}
            SeatAndDate5.append(p)
        # day["Number5"].append(Number_of_Seats5)

    for i in range(len(u)):
        Trip=Saturday.objects.all()[i].Trip
        print(Trip)
        if (Trip=="Township to Kota Station"):
            # print("True")
            Seats6A=Saturday.objects.all()[i].BookedSeats
            # print(Seats6A)
            Date6A=Saturday.objects.all()[i].Date
            p={"Seats": Seats6A, "date": Date6A}
            SeatAndDate6A.append(p)
        elif (Trip=="Kota Station to Township"):
        # Number_of_Seats6=Saturday.objects.all()[i].NumberOfSeats
            Seats6=Saturday.objects.all()[i].BookedSeats
            Date6=Saturday.objects.all()[i].Date
            p={"Seats": Seats6, "date": Date6}
            SeatAndDate6.append(p)
        # day["Number6"].append(Number_of_Seats6)

    for i in range(len(o)):
        Trip=Sunday.objects.all()[i].Trip
        print(Trip, "Done")
        if (Trip=="Township to Kota station"):
        # Number_of_Seats6=Saturday.objects.all()[i].NumberOfSeats
            Seats7A=Sunday.objects.all()[i].BookedSeats
            print(Seats7A)
            Date7A=Sunday.objects.all()[i].Date
            p={"Seats": Seats7A, "date": Date7A}
            SeatAndDate7A.append(p)
            
        elif (Trip=="Kota station to Township"):
        # Number_of_Seats6=Saturday.objects.all()[i].NumberOfSeats
            Seats7=Sunday.objects.all()[i].BookedSeats
            Date7=Sunday.objects.all()[i].Date
            p={"Seats": Seats7, "date": Date7}
            SeatAndDate7.append(p)

    # print(day)
    # print(SeatAndDate7A)
    name_user=request.session['EmployeeName']
    Mobile_user=request.session['EmployeeMobile']
    Code=request.session['Code']
    data={"name": name_user, "Mobile": Mobile_user, "Code": Code}
    MainData={"data": data, "day":day}
    # print(MainData)
    MainData=json.dumps(MainData)
    # print(data)
    # print(type(MainData))
    return render(request, "SeatAllocation/bookings.html", {"data":MainData})

def BookingsAdmin(request):
    x=Monday.objects.all()
    w=Tuesday.objects.all()
    e=Wednessday.objects.all()
    r=Thursday.objects.all()
    t=Friday.objects.all()
    u=Saturday.objects.all()
    o=Sunday.objects.all()
    SeatAndDate=[]
    SeatAndDate2A=[]
    SeatAndDate2B=[]
    SeatAndDate2=[]
    SeatAndDate3A=[]
    SeatAndDate3=[]
    SeatAndDate4A=[]
    SeatAndDate4B=[]
    SeatAndDate4=[]
    SeatAndDate5A=[]
    SeatAndDate5B=[]
    SeatAndDate5=[]
    SeatAndDate6A=[]
    SeatAndDate6=[]
    SeatAndDate7A=[]
    SeatAndDate7=[]


    day={"BookedSeats1": SeatAndDate, "BookedSeats2A": SeatAndDate2A, "BookedSeats2B": SeatAndDate2B,
         "BookedSeats2": SeatAndDate2, "BookedSeats3A": SeatAndDate3A, "BookedSeats3": SeatAndDate3, "BookedSeats4A": SeatAndDate4A, "BookedSeats4B": SeatAndDate4B
         ,"BookedSeats4": SeatAndDate4, "BookedSeats5A": SeatAndDate5A, "BookedSeats5B": SeatAndDate5B, "BookedSeats5": SeatAndDate5, 
         "BookedSeats6A": SeatAndDate6A, "BookedSeats6": SeatAndDate6, "BookedSeats7A": SeatAndDate7A, "BookedSeats7": SeatAndDate7}
    
    

    for i in range(len(x)):
        Seats1=Monday.objects.all()[i].BookedSeats
        Date1=Monday.objects.all()[i].Date
        p={"Seats": Seats1, "date": Date1}
        SeatAndDate.append(p)

    for i in range(len(w)):
        # Number_of_Seats2=Tuesday.objects.all()[i].NumberOfSeats
        Trip=Tuesday.objects.all()[i].Trip
        Time=Tuesday.objects.all()[i].Time
        

        # print(Trip)
        if (Trip=="Kota Station to Township"):
            if (Time=="8:00AM"):
                Seats2A=Tuesday.objects.all()[i].BookedSeats
                Date2A=Tuesday.objects.all()[i].Date
                p={"Seats": Seats2A, "date": Date2A}
                SeatAndDate2A.append(p)
            elif (Time=="8:30PM"):
                Seats2B=Tuesday.objects.all()[i].BookedSeats
                Date2B=Tuesday.objects.all()[i].Date
                p={"Seats": Seats2B, "date": Date2B}
                SeatAndDate2B.append(p)
            elif (Trip=="Township to Kota Station"):
                Seats2=Tuesday.objects.all()[i].BookedSeats
                Date2=Tuesday.objects.all()[i].Date
                p={"Seats": Seats2, "date": Date2}
                SeatAndDate2.append(p)
        # day["Number2"].append(Number_of_Seats2)
       
    for i in range(len(e)):
        # Number_of_Seats3=Monday.objects.all()[i].NumberOfSeats
        Trip=Wednessday.objects.all()[i].Trip
        
        if (Trip=="Township to Kota Station"):
            Seats3A=Wednessday.objects.all()[i].BookedSeats
            Date3A=Wednessday.objects.all()[i].Date
            p={"Seats": Seats3A, "date": Date3A}
            SeatAndDate3A.append(p)
        elif (Trip=="Kota Station to Township"):
            Seats3=Wednessday.objects.all()[i].BookedSeats
            Date3=Wednessday.objects.all()[i].Date
            p={"Seats": Seats3, "date": Date3}
            SeatAndDate3.append(p)
        # day["Number3"].append(Number_of_Seats3)

    for i in range(len(r)):
        Trip=Thursday.objects.all()[i].Trip

        # Number_of_Seats4=Thursday.objects.all()[i].NumberOfSeats
        if (Trip=="Township to Kota Station"):
            Seats4=Thursday.objects.all()[i].BookedSeats
            Date4=Thursday.objects.all()[i].Date
            p={"Seats": Seats4, "date": Date4}
            SeatAndDate4.append(p)
        elif (Trip=="Township to Baran"):
            Seats4A=Thursday.objects.all()[i].BookedSeats
            Date4A=Thursday.objects.all()[i].Date
            p={"Seats": Seats4A, "date": Date4A}
            SeatAndDate4A.append(p)
        elif (Trip=="Baran to Township"):
            Seats4B=Thursday.objects.all()[i].BookedSeats
            Date4B=Thursday.objects.all()[i].Date
            p={"Seats": Seats4B, "date": Date4B}
            SeatAndDate4B.append(p)
        # day["Number4"].append(Number_of_Seats4)

    for i in range(len(t)):
        Trip=Friday.objects.all()[i].Trip
        Time=Friday.objects.all()[i].Time
        # print(Trip)
        if (Trip=="Kota Station to Township"):
            if (Time=="8:00AM"):
                Seats5A=Friday.objects.all()[i].BookedSeats
                Date5A=Friday.objects.all()[i].Date
                p={"Seats": Seats5A, "date": Date5A}
                SeatAndDate5A.append(p)
            elif (Time=="8:30PM"):
                Seats5B=Friday.objects.all()[i].BookedSeats
                Date5B=Friday.objects.all()[i].Date
                p={"Seats": Seats5B, "date": Date5B}
                SeatAndDate5B.append(p)
        elif (Trip=="Township to Kota Station"):
            # Number_of_Seats5=Friday.objects.all()[i].NumberOfSeats
            Seats5=Friday.objects.all()[i].BookedSeats
            Date5=Friday.objects.all()[i].Date
            p={"Seats": Seats5, "date": Date5}
            SeatAndDate5.append(p)
        # day["Number5"].append(Number_of_Seats5)

    for i in range(len(u)):
        Trip=Saturday.objects.all()[i].Trip
        print(Trip)
        if (Trip=="Township to Kota Station"):
            # print("True")
            Seats6A=Saturday.objects.all()[i].BookedSeats
            # print(Seats6A)
            Date6A=Saturday.objects.all()[i].Date
            p={"Seats": Seats6A, "date": Date6A}
            SeatAndDate6A.append(p)
        elif (Trip=="Kota Station to Township"):
        # Number_of_Seats6=Saturday.objects.all()[i].NumberOfSeats
            Seats6=Saturday.objects.all()[i].BookedSeats
            Date6=Saturday.objects.all()[i].Date
            p={"Seats": Seats6, "date": Date6}
            SeatAndDate6.append(p)
        # day["Number6"].append(Number_of_Seats6)

    for i in range(len(o)):
        Trip=Sunday.objects.all()[i].Trip
        print(Trip, "Done")
        if (Trip=="Township to Kota station"):
        # Number_of_Seats6=Saturday.objects.all()[i].NumberOfSeats
            Seats7A=Sunday.objects.all()[i].BookedSeats
            print(Seats7A)
            Date7A=Sunday.objects.all()[i].Date
            p={"Seats": Seats7A, "date": Date7A}
            SeatAndDate7A.append(p)
            
        elif (Trip=="Kota station to Township"):
        # Number_of_Seats6=Saturday.objects.all()[i].NumberOfSeats
            Seats7=Sunday.objects.all()[i].BookedSeats
            Date7=Sunday.objects.all()[i].Date
            p={"Seats": Seats7, "date": Date7}
            SeatAndDate7.append(p)

    name_user=request.session['EmployeeName']
    Mobile_user=request.session['EmployeeMobile']
    CodeAdmin=request.session['Code']
    data={"name": name_user, "Mobile": Mobile_user, "Code": CodeAdmin}
    MainData={"data": data, "day":day}
    # print(MainData)
    MainData=json.dumps(MainData)
    # print(data)
    # print(type(MainData))
    return render(request, "SeatAllocation/BookingsAdmin.html", {"data":MainData})

def AllAccess(request):
    name_user=request.session['EmployeeName'] 
    # CanBook=request.session.get('Cancel', False)
    x=Monday.objects.all()
    w=Tuesday.objects.all()
    e=Wednessday.objects.all()
    r=Thursday.objects.all()
    t=Friday.objects.all()
    u=Saturday.objects.all()
    o=Sunday.objects.all()
    g=[]
    h=[]
    j=[]
    cf=[]
    jk=[]
    kl=[]
    lm=[]

    maindata={"Monday": g, "Tuesday": h, "Wednessday": j, "Thursday": cf, "Friday": jk, "Saturday": kl, "Sunday": lm}




    for i in range(len(x)):
        name1=Monday.objects.all()[i].EmployeeName
        Mobile_Number=Monday.objects.all()[i].EmployeeMobile
        Seats=Monday.objects.all()[i].BookedSeats
        Code=Monday.objects.all()[i].Code
        trip=Monday.objects.all()[i].Trip
        times=Monday.objects.all()[i].Time
        purpose=Monday.objects.all()[i].Purpose
        Date=Monday.objects.all()[i].Date
        data={"Day": "Monday", "Name": name1, "Code": Code, "Seats": Seats, "trip": trip, "time": times, "purpose": purpose, "date": Date, "MobileNumber": Mobile_Number}

        g.append(data)

    for i in range(len(w)):
        name2=Tuesday.objects.all()[i].EmployeeName
        Mobile_Number2=Tuesday.objects.all()[i].EmployeeMobile

        Seats2=Tuesday.objects.all()[i].BookedSeats
        Code2=Tuesday.objects.all()[i].Code
        trip2=Tuesday.objects.all()[i].Trip
        time2=Tuesday.objects.all()[i].Time
        purpose2=Tuesday.objects.all()[i].Purpose
        Date2=Tuesday.objects.all()[i].Date

        data2={"Day": "Tuesday", "Name": name2,"Code": Code2, "Seats": Seats2, "trip": trip2, "time": time2, "purpose": purpose2, "date": Date2, "MobileNumber": Mobile_Number2}
        h.append(data2)

       
    for i in range(len(e)):
        name3=Wednessday.objects.all()[i].EmployeeName
        Mobile_Number3=Wednessday.objects.all()[i].EmployeeMobile

        Seats3=Wednessday.objects.all()[i].BookedSeats
        Code3=Wednessday.objects.all()[i].Code

        trip3=Wednessday.objects.all()[i].Trip
        time3=Wednessday.objects.all()[i].Time
        purpose3=Wednessday.objects.all()[i].Purpose
        Date3=Wednessday.objects.all()[i].Date

        data3={"Day": "Wednessday", "Name": name3, "Code": Code3,"Seats": Seats3, "trip": trip3, "time": time3, "purpose": purpose3, "date": Date3, "MobileNumber": Mobile_Number3}
        j.append(data3)


    for i in range(len(r)):

        name4=Thursday.objects.all()[i].EmployeeName
        Seats4=Thursday.objects.all()[i].BookedSeats
        Mobile_Number4=Thursday.objects.all()[i].EmployeeMobile

        Code4=Thursday.objects.all()[i].Code

        trip4=Thursday.objects.all()[i].Trip
        time4=Thursday.objects.all()[i].Time
        purpose4=Thursday.objects.all()[i].Purpose
        Date4=Thursday.objects.all()[i].Date

        data4={"Day": "Thursday", "Name": name4,"Code": Code4, "Seats": Seats4, "trip": trip4, "time": time4, "purpose": purpose4, "date": Date4, "MobileNumber": Mobile_Number4}
        cf.append(data4)


    for i in range(len(t)):

        name5=Friday.objects.all()[i].EmployeeName
        Mobile_Number5=Friday.objects.all()[i].EmployeeMobile

        Seats5=Friday.objects.all()[i].BookedSeats
        Code5=Thursday.objects.all()[i].Code

        trip5=Friday.objects.all()[i].Trip
        time5=Friday.objects.all()[i].Time
        purpose5=Friday.objects.all()[i].Purpose
        Date5=Friday.objects.all()[i].Date

        data5={"Day": "Friday" ,"Name": name5, "Code": Code5, "Seats": Seats5, "trip": trip5, "time": time5, "purpose": purpose5, "date": Date5, "MobileNumber": Mobile_Number5}
        jk.append(data5)


    for i in range(len(u)):
        name6=Saturday.objects.all()[i].EmployeeName
        Mobile_Number6=Saturday.objects.all()[i].EmployeeMobile

        Seats6=Saturday.objects.all()[i].BookedSeats
        Code6=Thursday.objects.all()[i].Code

        trip6=Saturday.objects.all()[i].Trip
        time6=Saturday.objects.all()[i].Time
        purpose6=Saturday.objects.all()[i].Purpose
        Date6=Saturday.objects.all()[i].Date

        data6={"Day": "Saturday",  "Name": name6,"Code": Code6, "Seats": Seats6, "trip": trip6, "time": time6, "purpose": purpose6, "date": Date6, "MobileNumber": Mobile_Number6}
        kl.append(data6)


    for i in range(len(o)):
        name7=Sunday.objects.all()[i].EmployeeName
        Mobile_Number7=Sunday.objects.all()[i].EmployeeMobile

        Seats7=Sunday.objects.all()[i].BookedSeats
        Code7=Thursday.objects.all()[i].Code

        trip7=Sunday.objects.all()[i].Trip
        time7=Sunday.objects.all()[i].Time
        purpose7=Sunday.objects.all()[i].Purpose
        Date7=Sunday.objects.all()[i].Date

        data7={"Day": "Sunday", "Name": name7,"Code": Code7, "Seats": Seats7, "trip": trip7, "time": time7, "purpose": purpose7, "date": Date7, "Mobile Number": Mobile_Number7}
        lm.append(data7)

    # print(maindata)
    Details={"name_user": name_user, "data": maindata}
    # print(Details)
    details=json.dumps(Details)

    time.sleep(1)
    return render(request, "SeatAllocation/AllAccess.html", {"user": details})

def logoutB(request):
    logout(request)
    time.sleep(1)
    return redirect('/')