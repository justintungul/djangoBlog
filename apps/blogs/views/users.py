from django.shortcuts import render

def index(request):
    # user =  User.objects.get(id = request.session['user_id'])
    # request.session['name'] = user.first_name.capitalize() + ' ' + user.last_name.capitalize()
    # request.session['email'] = user.email
    # context = {
    #     'customers': Customer.objects.all(),
    #     'projects': Project.objects.all()
    # }
    context = {
        'route': 'blogs/pages/home.html'
    }
    return render(request, 'blogs/index.html', context)

def about(request):
    context = {
        'route': 'blogs/pages/about.html'
    }
    return render(request, 'blogs/index.html', context)

def post(request):
    context = {
        'route': 'blogs/pages/post.html'
    }
    return render(request, 'blogs/index.html', context)

def contact(request):
    context = {
        'route': 'blogs/pages/contact.html'
    }
    return render(request, 'blogs/index.html', context)

def login(request):
    context = {
        'route': 'blogs/pages/login.html'
    }
    return render(request, 'blogs/index.html', context)