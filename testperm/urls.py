from django.urls import path
from .views import home, add_emp, ChangeEmp, ViewEmp


urlpatterns = [
    path('', home, name='home'),
    path('add', add_emp, name='add'),
    path('change/<pk>', ChangeEmp.as_view(), name='change'),
    path('view/<pk>', ViewEmp.as_view(), name='view'),
]