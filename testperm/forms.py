from django.forms import ModelForm
from testperm.models import Employee

class EmpForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'