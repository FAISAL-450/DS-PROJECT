from django.urls import path
from .views import home_view, root_redirect_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Redirects '/' to department-based dashboard
    path('', login_required(root_redirect_view, login_url='/auth/login/'), name='root_redirect'),

    # Direct view of the static home page
    path('home/', home_view, name='home'),
]


