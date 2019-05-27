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
        'ROUTE': 'blogs/pages/home.html'
    }
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

def login(request):
    context = {
        'ROUTE': 'blogs/pages/login.html',
        'CSS_ROUTE': 'blogs/css/login.css'
    }
    return render(request, 'blogs/index.html', context)

def register(request):
    context = {
        'ROUTE': 'blogs/pages/register.html',
        'CSS_ROUTE': 'blogs/css/register.css'
    }
    return render(request, 'blogs/index.html', context)
    