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

def contact(request):
    context = {
        'ROUTE': 'blogs/pages/contact.html',
        'CSS_ROUTE': 'blogs/css/contact.css'
    }
    return render(request, 'blogs/index.html', context)

def signin(request):
    context = {
        'ROUTE': 'blogs/pages/signin.html',
        'CSS_ROUTE': 'blogs/css/signin.css'
    }
    return render(request, 'blogs/index.html', context)

def register(request):
    context = {
        'ROUTE': 'blogs/pages/register.html',
        'CSS_ROUTE': 'blogs/css/register.css',
        'test': 'test'
    }
    if 'data' in request.session:
        context['data'] = request.session['data']
        del request.session['data']

    print(context)
    return render(request, 'blogs/index.html', context)
    