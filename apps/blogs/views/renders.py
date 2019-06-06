from django.shortcuts import render
from . import users
from ..models import *

def index(request):
    context = {
        'ROUTE': 'blogs/pages/home.html',
        'data': {
            'posts': Post.objects.all().order_by('-created_at')
        }
    }
    # get all blogs
    # add to context
    # context.update({'blogs': blogs})
    return render(request, 'blogs/index.html', context)

def about(request):
    context = {
        'ROUTE': 'blogs/pages/about.html'
    }
    return render(request, 'blogs/index.html', context)

def post(request):
    context = {
        'ROUTE': 'blogs/pages/post.html'
    }
    return render(request, 'blogs/index.html', context)

def post_new(request):
    context = {
        'ROUTE': 'blogs/pages/post_new.html',
        'CSS_ROUTE': 'blogs/css/pages/post_new.css',
        'JS_ROUTE': 'blogs/js/post_new.js',
    }
    return render(request, 'blogs/index.html', context)

def contact(request):
    context = {
        'ROUTE': 'blogs/pages/contact.html',
        'CSS_ROUTE': 'blogs/css/pages/contact.css'
    }
    return render(request, 'blogs/index.html', context)

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

def profile_personal(request):
    user = User.objects.get(id = request.session['user_id'])
    posts = Post.objects.filter(author = user)
    # print(posts.__dict__)
    context = {
        'ROUTE': 'blogs/pages/profile.html',
        'CSS_ROUTE': 'blogs/css/pages/profile.css',
        'data': {
            'posts': posts
        }
    }
    if 'data' in request.session:
        context['data'] = request.session['data']
        del request.session['data']
    return render(request, 'blogs/index.html', context)

def profile_public(request, user_id):
    user = User.objects.get(id = user_id)
    posts = Post.objects.filter(author = user)
    following = False
# 
    if User.objects.get(id = request.session['user_id']).following.all().filter(id = user.id):
        following = True

    context = {
        'ROUTE': 'blogs/pages/profile_public.html',
        'CSS_ROUTE': 'blogs/css/pages/profile_public.css',
        'data': {
            'user': user,
            'posts': posts,
            'following': following
        }
    }
    return render(request, 'blogs/index.html', context)
    