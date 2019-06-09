from django.shortcuts import render, redirect

from ..models import *


# Render methods
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
    
# Process methods
def profile_follow(request, user_id):
    if 'user_id' in request.session:
        user = User.objects.get(id = request.session['user_id'])
        user_to_follow = User.objects.get(id = user_id)

        user.following.add(user_to_follow)
        user.save()
        return redirect('/profile/' + user_id)
    else:
        return redirect('/signin')

def profile_unfollow(request, user_id):
    user = User.objects.get(id = request.session['user_id'])
    user_to_unfollow = User.objects.get(id = user_id)

    user.following.remove(user_to_unfollow)
    user.save()

    return redirect('/profile/' + user_id)