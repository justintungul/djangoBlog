from django.shortcuts import render, redirect

from ..models import *


# Render methods
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'ROUTE': 'blogs/pages/post.html',
        'data': {
            'post': post
        }
    }
    return render(request, 'blogs/index.html', context)

def post_sample(request):
    context = {
        'ROUTE': 'blogs/pages/post_sample.html',
        'data': {
            'post': post
        }
    }
    return render(request, 'blogs/index.html', context)

def post_new(request):
    context = {
        'ROUTE': 'blogs/pages/post_new.html',
        'CSS_ROUTE': 'blogs/css/pages/post_new.css',
        'JS_ROUTE': 'blogs/js/post_new.js',
    }
    return render(request, 'blogs/index.html', context)

# Process methods
def create_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES)
        if postForm.is_valid():
            post = Post(**postForm.cleaned_data)
            post.author = User.objects.get(id = request.session['user_id'])
            post.save()
            return redirect('/profile')
        else:
            request.session['data'] = {'error': 'error'}
            return renders.post_new(request)
# File upload 
# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html