from django.shortcuts import render, redirect

from . import users
from ..models import *


# Render methods
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

def contact(request):
    context = {
        'ROUTE': 'blogs/pages/contact.html',
        'CSS_ROUTE': 'blogs/css/pages/contact.css'
    }
    return render(request, 'blogs/index.html', context)