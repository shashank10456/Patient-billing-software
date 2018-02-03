from django.http import HttpResponse
from .models import PatientDetails,BillDetails
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
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
        brno = request.POST.get('brno', False)
        z = PatientDetails.objects.get(rno=brno)
        bedno = request.POST.get('bedno',False)
        wardno = request.POST.get('wardno',False)
        amt = request.POST.get('amt',False)
        pd = BillDetails.objects.create(
            brno=z,
            bedno=bedno,
            wardno=wardno,
            amt=amt,
        )

        return redirect('home')  # TODO: redirect to the created topic page

    return render(request, 'bill_details.html')

def treatments_needed(request):
    return render(request,'treatments_needed.html')

def general(request):
    ol=BillDetails.objects.all()
    l=list()
    for x in ol:
        l.append(x.bedno)
    return render(request,'general.html',{'l':l,'range':range(20)})
