from django.conf.urls import url
from .views import users
from .views import posts
from .views import renders

urlpatterns = [
    # render routes
    url(r'^$', renders.index),
    url(r'^about$', renders.about),
    url(r'^contact$', renders.contact),
    url(r'^profile$', renders.profile_personal),
    url(r'^profile/following$', renders.profile_following),
    url(r'^profile/(?P<user_id>\d+)$', renders.profile_public),

    # user routes
    url(r'^register$', renders.register),
    url(r'^register/submit$', users.create_user),
    url(r'^signin$', renders.signin),
    url(r'^signin/user$', users.signin_user),
    url(r'^logout$', users.logout),
    url(r'^profile/follow/(?P<user_id>\d+)$', users.profile_follow),
    url(r'^profile/unfollow/(?P<user_id>\d+)$', users.profile_unfollow),

    # post
    url(r'^post/sample$', renders.post_sample),
    url(r'^post/(?P<post_id>\d+)$', renders.post),
    url(r'^post/new$', renders.post_new),
    url(r'^post/submit$', posts.create_post),
]