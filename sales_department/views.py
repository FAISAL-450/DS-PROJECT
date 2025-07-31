from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_sales_user

@login_required
@user_passes_test(is_sales_user)
def sales_department_view(request):
    return render(request, 'sales_department/sales_department.html')

