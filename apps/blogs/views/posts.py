from django.shortcuts import render, redirect
from ..models import *
from . import renders 

def create_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        print(postForm)
        if postForm.is_valid():
            post = Post(**postForm.cleaned_data)
            post.author = User.objects.get(id = request.session['user_id'])
            post.save()
            return redirect('/profile')
        else:
            request.session['data'] = {'error': 'error'}
            return renders.post_new(request)