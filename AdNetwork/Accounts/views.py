from django.shortcuts import render

# Create your views here.
def login(request):

    return render(request, 'accounts/login.html')

def signup(request):

    return render(request, 'accounts/signup.html')

def confirmation(request):

    return render(request,'accounts/confirmation.html')

def recovery(request):

    return render(request,'accounts/recovery.html')

