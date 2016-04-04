from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<id>[0-9]+)$',views.article_detail,name='article'),
    url(r'^post_a_blog$',views.post_a_blog,name='post_blog'),
    url(r'^article/post_a_comment/(?P<id>[0-9]+)$',views.post_a_comment,name='post_comment'),
    url(r'^article/show_comments/(?P<id>[0-9]+)$',views.show_comments,name='show_comment'),
]
