"""
URL configuration for ds_garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from home.views import root_redirect_view  # Your view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(root_redirect_view), name='home_redirect'),
    path('construction-department/', include('construction_department.urls')),
    path('sales-department/', include('sales_department.urls')),
    path('auth/', include('azure_auth.urls')),
]


