from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_post, name='list_of_post'),
    url(r'^reminder/(?P<reminder_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^newreminder/', views.new_reminder, name="new_reminder"),

]
