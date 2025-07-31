from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    # This is your public homepage view
    return render(request, 'home/home.html')

@login_required
def root_redirect_view(request):
    # Redirect users based on their group membership
    user = request.user
    if user.groups.filter(name="Construction").exists():
        return redirect("construction_department:dashboard")
    elif user.groups.filter(name="Sales").exists():
        return redirect("sales_department:dashboard")
    else:
        # Fallback for users not in those groups
        return redirect("/auth/access-denied/")



