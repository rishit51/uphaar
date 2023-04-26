from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegistrationForm
# Create your views here.
def index (request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully!')
            return redirect('home-home')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})
    
   
