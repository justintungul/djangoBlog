from django.conf.urls import url
from .views import users

urlpatterns = [
    url(r'^$', users.index),
    url(r'^about$', users.about),
    url(r'^post$', users.post),
    url(r'^contact$', users.contact),
    url(r'^login$', users.login),
    # # render routes
    # url(r'^$', views.index, name='index'),
    # url(r'^project/(?P<proj_id>\d+)$', views.proj_timeline),
    # url(r'^project/(?P<proj_id>\d+)/timeline$', views.proj_timeline),
    # url(r'^project/(?P<proj_id>\d+)/messages$', views.proj_messages),
    # url(r'^project/(?P<proj_id>\d+)/files$', views.proj_files),
    # url(r'^project/(?P<proj_id>\d+)/tasks$', views.proj_tasks),
    # url(r'^project/item/(?P<item_id>\d+)$', views.proj_item_show),
    # # submit routes
    # url(r'^users/api$', views.users_api),
    # url(r'^project/submit$', views.proj_submit),
    # url(r'^item/submit$', views.item_submit),
    # url(r'^revision/submit$', views.revision_submit),
    # url(r'^comment/submit$', views.comment_submit),
    # url(r'^message/submit$', views.message_submit),
    # url(r'^reply/submit$', views.reply_submit),
    # # settings area
    # url(r'^settings/profile$', views.settings_profile),
]