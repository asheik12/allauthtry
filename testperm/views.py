from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from testperm.forms import EmpForm 
from django.views.generic import UpdateView, DetailView
from testperm.models import Employee
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

def home(request):
    context = Employee.emp.all()
    return render(request, 'home.html', {'context': context})

@login_required
@permission_required('testperm.add_employee')
def add_emp(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EmpForm()
    return render(request, 'add_emp.html', {'form': form})

# @method_decorator(login_required, name='dispatch')
class ChangeEmp(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'change_emp.html'    
    context_object_name = 'context' 
    success_url = reverse_lazy('home')
    permission_required = ('testperm.change_employee',)

# @method_decorator(login_required, name='dispatch')
class ViewEmp(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    context_object_name = 'context' 
    template_name = 'view_emp.html'
    permission_required = ('testperm.view_employee',)