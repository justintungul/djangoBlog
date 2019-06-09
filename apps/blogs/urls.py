from django.conf.urls import url

# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
from .views import *

urlpatterns = [
    # general routes
    url(r'^$', general.index),
    url(r'^about$', general.about),
    url(r'^contact$', general.contact),

    # user routes
    url(r'^register$', users.register),
    url(r'^register/submit$', users.create_user),
    url(r'^signin$', users.signin),
    url(r'^signin/user$', users.signin_user),
    url(r'^logout$', users.logout),

    # profiles
    url(r'^profile$', profiles.profile_personal),
    url(r'^profile/following$', profiles.profile_following),
    url(r'^profile/(?P<user_id>\d+)$', profiles.profile_public),
    url(r'^profile/follow/(?P<user_id>\d+)$', profiles.profile_follow),
    url(r'^profile/unfollow/(?P<user_id>\d+)$', profiles.profile_unfollow),

    # posts
    url(r'^post/sample$', posts.post_sample),
    url(r'^post/(?P<post_id>\d+)$', posts.post),
    url(r'^post/new$', posts.post_new),
    url(r'^post/submit$', posts.create_post),
]