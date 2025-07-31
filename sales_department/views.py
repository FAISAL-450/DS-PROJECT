# views.py inside sales_department
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .permissions import is_sales_user

@user_passes_test(is_sales_user)
def sales_department_view(request):
    return render(request, 'sales_department/sales_department.html')

