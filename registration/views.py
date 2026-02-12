from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib.auth.hashers import make_password


def registration_form(request):
    """Handle registration form display and submission"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Get cleaned data
            data=form.cleaned_data
            hashPass= make_password(data['password'])
            registration=Registration(
                name=data['name'],email=data['email'],password=hashPass
            )
            registration.save() 
            print("success")
            return render(request, 'registration/form.html',
                          {
                              'form':form,
                              "success":"Successful"
                          })
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})