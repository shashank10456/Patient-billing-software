from django.http import HttpResponse
from .models import PatientDetails,BillDetails,Transfers,PatientTreatments,Treatment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from itertools import chain
def home(request):
    ol = PatientDetails.objects.all()
    return render(request, 'home.html',{'ol':ol})

def start(request):
    return render(request, 'start.html')

def patient_registration(request) :
    if request.method == 'POST':
        rno = request.POST.get('rno', False)
        pname = request.POST.get('pname',False)
        sex = request.POST.get('sex',False)
        contact_no = request.POST.get('contact_no',False)
        addr = request.POST.get('addr',False)
        age = request.POST.get('age',False)
        pd = PatientDetails.objects.create(
            rno=rno,
            pname=pname,
            sex=sex,
            contact_no=contact_no,
            addr=addr,
            age=age
        )

        return redirect('home')  # TODO: redirect to the created topic page

    return render(request, 'patient_registration.html')

def bill_details(request):

    if request.method == 'POST':
        check=True
        brno = request.POST.get('brno', False)
        z = PatientDetails.objects.get(rno=brno)
        if BillDetails.objects.filter(brno_id=z).exists() is False:
            bedno = request.POST.get('bedno',False)
            wardno = request.POST.get('wardno',False)
            amt = request.POST.get('amt',False)
            pd = BillDetails.objects.create(
                brno=z,
                bedno=bedno,
                wardno=wardno,
                amt=amt,
                )
        else :
            return HttpResponse('Sorry, You have already been alloted a bed!')

        return redirect('home')  # TODO: redirect to the created topic page

    return render(request, 'bill_details.html')

def treatments_needed(request):
    ol=Treatment.objects.all()
    if request.method == 'POST':
        prno = request.POST.get('prno', False)
        if True:
            z = PatientDetails.objects.get(rno=prno)
            ptid = request.POST.get('ptid',False)
            z1 = Treatment.objects.get(tid=ptid)
            tr = PatientTreatments.objects.create(
                prno=z,
                ptid=z1,
                )

            return redirect('home')  # TODO: redirect to the created topic page

    return render(request, 'treatments_needed.html',{'ol':ol,'range':range(5)})

def general(request):
    ol=BillDetails.objects.all()
    l=list()
    for x in ol:
        if x.wardno== '1':
            l.append(x.bedno)
    return render(request,'general.html',{'l':l,'range':range(50)})

def icu(request):
    ol=BillDetails.objects.all()
    l=list()
    for x in ol:
        if x.wardno == '2' :
            l.append(x.bedno)
    return render(request,'general.html',{'l':l,'range':range(50)})

def transfers(request):

    if request.method == 'POST':
        check=True
        brno = request.POST.get('brno', False)
        z = PatientDetails.objects.get(rno=brno)
        if BillDetails.objects.filter(brno_id=z).exists() is True:
            bedno = request.POST.get('bedno',False)
            wardno = request.POST.get('wardno',False)
            amt1 = request.POST.get('amt',False)
            obj=BillDetails.objects.get(brno_id=z)
            x=obj.amt
            obj.amt=int(x)+int(amt1)
            obj.bedno=bedno
            obj.wardno=wardno
            obj.save()

        else :
            return HttpResponse('Sorry, You have already been alloted a bed!')

        return redirect('home')  # TODO: redirect to the created topic page

    return render(request, 'bill_details.html')



def bill_generator(request):
    l=list()
    l1=list()
    treatment_cost=0
    if request.method == 'POST':
        check=True
        timediff=datetime.now(timezone.utc)-datetime.now(timezone.utc)
        bno=0

        brno = request.POST.get('brno', False)
        pd = PatientDetails.objects.get(rno=brno)
        ptr=PatientTreatments.objects.filter(prno=15)
        bd=BillDetails.objects.get(brno_id=15)

        if BillDetails.objects.filter(brno_id=pd).exists() is True:
            bd=BillDetails.objects.get(brno_id=pd)
            timediff = datetime.now(timezone.utc)-bd.btime
            bno=bd.wardno
        if PatientTreatments.objects.filter(prno=pd).exists() is True:
            ptr=PatientTreatments.objects.filter(prno=pd)

        for obj in ptr:
            l.append(obj.ptid)
            treatment_cost=treatment_cost+obj.ptid.tcost


        diff_sec=timediff.total_seconds()
        ward_cost=diff_sec * 1000
        ward_cost=int(ward_cost/86400)
        days=int(diff_sec/86400)
        print(bd.brno_id)

        if bd.wardno==2:
            ward_cost=ward_cost*2
        if bd.brno_id==15:
            ward_cost=0
            days=0
            bno=0
        total_cost=treatment_cost+ward_cost
        remaining_amt=total_cost-bd.amt
        if ward_cost!=0:
            BillDetails.objects.filter(brno_id=pd).delete()
        if treatment_cost!=0:
            PatientTreatments.objects.filter(prno=pd).delete()
        return render(request,'bill_generator2.html',{'days':days,'ward_cost':ward_cost,'wardno':bno,'l':l,'total_cost':total_cost,'paid':bd.amt,'remaining_amt':remaining_amt})  # TODO: redirect to the created topic page

    return render(request, 'bill_generator.html')

def all_patient_details(request):
    pd=list()
    bd=list()
    bd=BillDetails.objects.all()
    for obj in bd:
        pd.append(PatientDetails.objects.get(id=obj.brno_id))
    l=zip(bd,pd)
    for x,y in l:
        print(x.wardno," x ",y.rno,"  y.rno  ")
    return render(request,'all_patient_details.html',{'l':l})
