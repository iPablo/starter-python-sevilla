from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^posts/$', views.PostsView.as_view(), name='posts_lists'),
    url(r'^posts/create/$', views.PostCreateView.as_view(), name='post_create'),
]

