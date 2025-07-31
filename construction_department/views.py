from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_construction_user

@login_required
@user_passes_test(is_construction_user)
def construction_department_view(request):
    return render(request, 'construction_department/construction_department.html')




