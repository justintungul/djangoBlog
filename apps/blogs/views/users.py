from django.shortcuts import render

def index(request):
    # user =  User.objects.get(id = request.session['user_id'])
    # request.session['name'] = user.first_name.capitalize() + ' ' + user.last_name.capitalize()
    # request.session['email'] = user.email
    # context = {
    #     'customers': Customer.objects.all(),
    #     'projects': Project.objects.all()
    # }
    return render(request, 'blogs/pages/index.html')

def about(request):
    return render(request, 'blogs/pages/about.html')

def post(request):
    return render(request, 'blogs/pages/post.html')

def contact(request):
    return render(request, 'blogs/pages/contact.html')