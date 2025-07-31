from django.shortcuts import redirect

def azure_login(request):
    # Redirect to Azure AD login or process token
    return redirect("https://login.microsoftonline.com/your-tenant-id/oauth2/authorize")

