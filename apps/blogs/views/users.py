from django.shortcuts import render, redirect

from .helpers import sessions
from ..models import *


# Render methods
def signin(request):
    context = {
        'ROUTE': 'blogs/pages/signin.html',
        'CSS_ROUTE': 'blogs/css/pages/signin.css'
    }
    return render(request, 'blogs/index.html', context)

def register(request):
    context = {
        'ROUTE': 'blogs/pages/register.html',
        'CSS_ROUTE': 'blogs/css/pages/register.css',
        'test': 'test'
    }
    if 'data' in request.session:
        context['data'] = request.session['data']
        del request.session['data']

    print(context)
    return render(request, 'blogs/index.html', context)

# Process methods
def create_user(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            # create and save user from cleaned form data
            user = User(**userForm.cleaned_data)
            user.create_password_hash()
            user.save()
            return redirect('/')
        else:
            # render form with errors
            request.session['data'] = {'error': 'error'}
            return redirect('/register')

def signin_user(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST['email'])
        except Exception as e:
            print(str(e))
            # messages.error(request, 'Unable to login')
            return redirect('/signin')

        if (user.verify_password_hash(request.POST['password'])):
            sessions.create_user_session(request, user)
            return redirect('/')
        else:
            # messages.error(request, 'Unable to login')
            return redirect('/signin')

def logout(request):
    keys = []
    
    for key in request.session.keys():
        keys.append(key)

    for idx in range(len(keys)):
        del request.session[keys[idx]]

    # messages.success(request, 'You\'ve been logged out successfully!')
    return redirect('/signin')