from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

from .forms import customizedForm



def home(request):
    return render(request, 'home.html')


def register(request):

    """
    a function to register users using customized Usercreationform function in forms.py
    args: request

    returns: the html registration form
    """

    form=customizedForm()

    
    if request.method=='POST':
        form=customizedForm(request.POST)

        
        if form.is_valid():
            form.save()
            messages.success(request, "User account created successfuly")
            return redirect('login')

    context={'form':form}
    return render(request, "register.html", context)


#login function

def signin(request):

    if request.method=='POST':
        identifier=request.POST.get("identifier")
        password=request.POST.get("password")

        user=authenticate(request, username=identifier,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
        
    return render(request, "login.html")

    
    

    

    


    