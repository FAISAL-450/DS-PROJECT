from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from azure_auth.helpers import has_role

def home_view(request):
    return render(request, 'home/home.html')  # Adjust template path if needed

@login_required(login_url='/auth/login/')
def root_redirect_view(request):
    user = request.user

    if has_role(user, "ConstructionGroup"):
        return redirect("/construction/dashboard/")
    elif has_role(user, "SalesGroup"):
        return redirect("/sales/dashboard/")
    else:
        return redirect("/auth/login/")  # Fallback if no role matches

