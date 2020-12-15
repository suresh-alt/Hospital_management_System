from django.shortcuts import render,redirect
from app.forms import *
from app.models import *

# Create your views here.
def show(request):
    return render(request,'app/index.html')


def checklogin(request):
    un=request.POST.get('t1')
    pa=request.POST.get('t2')

    if un == 'suresh' and pa == '12345':
        return render(request,'app/home.html')


def home(request):
    return render(request,'app/home.html')


def addp(request):
    return render(request,"app/addpatient.html",{"form":PatientForm()})


def savep(request):
    pf=PatientForm(request.POST)
    if pf.is_valid():
        pf.save()
        return redirect('addp')
    else:
        return render(request,"app/addpatient.html",{"form":pf})


def addd(request):
    return render(request,'app/Adddoctor.html',{"form":DoctorForm()})
    return None


def saved(request):
    df=DoctorForm(request.POST)
    if df.is_valid():
        df.save()
        return redirect('addd')
    else:
        return render(request,"app/Adddoctor.html",{"form":df})


def addt(request):
    return render(request,'app/Addtest.html',{"form":TestForm()})


def savet(request):
    tf=TestForm(request.POST)
    if tf.is_valid():
        tf.save()
        return redirect('addt')
    else:
        return render(request,'app/Addtest.html',{"form":tf})


def addap(request):
    return render(request,'app/Addappointment.html',{"form":AppointmentForm()})


def saveap(request):
    af=AppointmentForm(request.POST)

    if af.is_valid():
        af.save()
        return redirect('addap')
    else:
        return render(request,'app/Addappointment.html',{"form":af})


def addc(request):
   return render(request,'app/adddiscarge.html',{"form":DischargeForm()})


def savedc(request):
    dc = DischargeForm(request.POST)

    if dc.is_valid():
        dc.save()
        return redirect('addc')
    else:
        return render(request, 'app/adddiscarge.html', {"form":dc})


def viewp(request):
    return render(request,'app/viewpatient.html',{"data":PatientModel.objects.all()})


def up(request):
    return render(request,"app/Updatepatient.html",{'data':PatientModel.objects.get(Patient_id=request.GET.get('pid'))})


def saveup(request):
    pid=request.POST.get('t1')
    pna=request.POST.get('t2')
    cnic=request.POST.get('t3')
    pra=request.POST.get('t4')
    gen=request.POST.get('t5')
    age=request.POST.get('t6')
    cno=request.POST.get('t7')
    add=request.POST.get('t8')
    PatientModel(Patient_id=pid,Patient_name=pna,CNIC=cnic,Relative_Name=pra,gender=gen,Age=age,Mobile=cno,Address=add).save()
    return redirect('viewp')


def delp(request):
    PatientModel.objects.get(Patient_id=request.GET.get('pid')).delete()
    return redirect('viewp')


def viewd(request):
    return render(request, 'app/viewdoctor.html', {"data": DoctorModel.objects.all()})



def updated(request):
    return render(request,"app/Updatedoctor.html",{'data':DoctorModel.objects.get(Doctor_id=request.GET.get('pid'))})


def saveupdatedoctor(request):
    did = request.POST.get('t1')
    dna = request.POST.get('t2')
    cno = request.POST.get('t3')
    otime = request.POST.get('t4')
    odays = request.POST.get('t5')
    spcl = request.POST.get('t6')
    DoctorModel(Doctor_id=did,Doctor_name=dna,Mobile=cno,OPT_Time=otime,OPD_Days=odays,Specialization=spcl).save()
    return redirect('viewd')

def deld(request):
    DoctorModel.objects.get(Doctor_id=request.GET.get('pid')).delete()
    return redirect('viewd')


def viewt(request):
    return render(request,'app/viewt.html',{"data":testModel.objects.all()})


def delt(request):
    x=request.GET.get('no')
    print(x)
    testModel.objects.get(Test_No=x).delete()
    return redirect('viewt')


def viewapt(request):
    return render(request,'app/viewappointment.html',{"data":AppointmentModel.objects.all()})


def delapt(request):
    AppointmentModel.objects.get(Patient_id=request.GET.get('x')).delete()
    return redirect('viewapt')


def viewdc(request):
    return render(request,'app/viewdiscarge.html',{"data":DischargeModel.objects.all()})


def deldc(request):
    DischargeModel.objects.get(s_no=request.GET.get('no')).delete()
    return redirect('viewdc')