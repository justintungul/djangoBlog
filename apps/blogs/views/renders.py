from django.shortcuts import render, redirect
from . import users
from ..models import *

def index(request):
    context = {
        'ROUTE': 'blogs/pages/home.html',
        'data': {
            'posts': Post.objects.all().order_by('-created_at')
        }
    }
    return render(request, 'blogs/index.html', context)

def about(request):
    context = {
        'ROUTE': 'blogs/pages/about.html'
    }
    return render(request, 'blogs/index.html', context)

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
    posts = User.objects.get(id = request.session['user_id']).posts.all().order_by('-created_at')
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
    following = None

    if 'user_id' in request.session:
        if user == User.objects.get(id = request.session['user_id']):
            return redirect('/profile')
        elif User.objects.get(id = request.session['user_id']).following.all().filter(id = user.id):
            following = True

    context = {
        'ROUTE': 'blogs/pages/profile.html',
        'CSS_ROUTE': 'blogs/css/pages/profile.css',
        'data': {
            'user': user,
            'posts': user.posts.all().order_by('-created_at'),
            'following': following
        }
    }
    return render(request, 'blogs/index.html', context)


def profile_following(request):
    following = User.objects.get(id=request.session['user_id']).following.all()
    posts = Post.objects.filter(author__in=following).order_by('-created_at')
    print(posts)

    context = {
        'ROUTE': 'blogs/pages/profile.html',
        'CSS_ROUTE': 'blogs/css/pages/profile.css',
        'data': {
            'posts': posts
        }
    }
    return render(request, 'blogs/index.html', context)