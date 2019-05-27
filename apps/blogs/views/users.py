from django.shortcuts import render, redirect
from ..models import *
from . import renders 

def create_user(request):
    if request.method == 'POST':
        print('======================================')
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            # create and save user from cleaned form data
            print(userForm.cleaned_data)
            user = User(**userForm.cleaned_data)
            user.createHash()
            user.save()
            return redirect('/')
        else:
            pass
            # render form with errors
            request.session['data'] = {'error': 'error'}
            return renders.register(request)