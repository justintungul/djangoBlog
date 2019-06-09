from django.shortcuts import render, redirect
from .helpers import sessions
from ..models import *
from . import renders 

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
            return renders.register(request)

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

def profile_follow(request, user_id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        user_to_follow = User.objects.get(id = user_id)

        user.following.add(user_to_follow)
        user.save()
        return redirect('/profile/' + user_id)
    else:
        return redirect('/signin')

def profile_unfollow(request, user_id):
    user = User.objects.get(id = request.session['user_id'])
    user_to_unfollow = User.objects.get(id = user_id)

    user.following.remove(user_to_unfollow)
    user.save()

    return redirect('/profile/' + user_id)