from django.db import models

# Create your models here.
class PatientModel(models.Model):
    Patient_id=models.AutoField(primary_key=True)
    Patient_name=models.CharField(max_length=30)
    CNIC=models.IntegerField(unique=True)
    Relative_Name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    Age=models.IntegerField()
    Mobile=models.IntegerField(unique=True)
    Address=models.CharField(max_length=30)

    def __str__(self):
        return self.Patient_name
class DoctorModel(models.Model):
    Doctor_id=models.IntegerField(primary_key=True)
    Doctor_name=models.CharField(max_length=30)
    Mobile=models.IntegerField()
    OPT_Time=models.CharField(max_length=30)
    OPD_Days=models.CharField(max_length=30)
    Specialization=models.CharField(max_length=30)
    def __str__(self):
        return self.Doctor_name
class testModel(models.Model):
    Test_No=models.AutoField(primary_key=True)
    Test_name=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.Test_name

class AppointmentModel(models.Model):
    Doctor=models.OneToOneField(DoctorModel,on_delete=models.CASCADE)
    Patient=models.OneToOneField(PatientModel,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()

class DischargeModel(models.Model):
    s_no=models.AutoField(primary_key=True)
    Patient_name=models.OneToOneField(PatientModel,on_delete=models.CASCADE)
    Disease=models.OneToOneField(testModel,on_delete=models.CASCADE)
    Discarged_By=models.OneToOneField(DoctorModel,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.DateTimeField()
