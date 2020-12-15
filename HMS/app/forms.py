from django import forms
from app.models import *

class PatientForm(forms.ModelForm):
    g=(('male','MALE'),('female','FEMALE'),('others','OTHERS'))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    class Meta:
        model=PatientModel
        fields="__all__"

class DoctorForm(forms.ModelForm):
    class Meta:
        model=DoctorModel
        fields="__all__"

class TestForm(forms.ModelForm):
    class Meta:
        model=testModel
        fields="__all__"

class AppointmentForm(forms.ModelForm):
    Time=forms.TimeField()
    class Meta:
        model=AppointmentModel
        fields="__all__"


class DischargeForm(forms.ModelForm):
    class Meta:
        model=DischargeModel
        fields="__all__"