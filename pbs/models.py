from django.db import models
from django.contrib.auth.models import User


class PatientDetails(models.Model):
    pname = models.TextField(max_length=30)
    rno=models.TextField(max_length=10, unique=True)
    contact_no=models.TextField(max_length=13)
    addr=models.TextField(max_length=50)
    sex=models.TextField(max_length=7)
    age=models.TextField(max_length=5)


class Treatment(models.Model):
    tid = models.CharField(max_length=30, unique=True)
    tname = models.TextField(max_length=50)
    tcost=models.IntegerField()


class BillDetails(models.Model):
    brno=models.ForeignKey(PatientDetails , related_name='billdetails')
    wardno = models.TextField(max_length=30)
    bedno=models.IntegerField()
    amt = models.IntegerField()
    btime = models.DateTimeField(auto_now_add=True)


class PatientTreatments(models.Model):
    prno=models.ForeignKey(PatientDetails , related_name='ptr1')
    ptid=models.ForeignKey(Treatment , related_name='ptr2')


class Transfers(models.Model):
    trno=models.ForeignKey(PatientDetails , related_name='transfers')
    trid=models.IntegerField()

def __str__(self):
        return self.name
