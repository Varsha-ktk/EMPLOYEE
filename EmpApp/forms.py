from django import forms

from EmpApp.models import Employee


class EmpDet(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"



