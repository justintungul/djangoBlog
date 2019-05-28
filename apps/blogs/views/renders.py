from django.shortcuts import render
from . import users

def index(request):
    context = {
        'ROUTE': 'blogs/pages/home.html'
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
        'CSS_ROUTE': 'blogs/css/pages/post_new.css'
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

def profile(request):
    context = {
        'ROUTE': 'blogs/pages/profile.html',
        'CSS_ROUTE': 'blogs/css/pages/profile.css',
    }
    if 'data' in request.session:
        context['data'] = request.session['data']
        del request.session['data']
    return render(request, 'blogs/index.html', context)
    