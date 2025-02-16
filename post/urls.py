from django.urls import path
from .views import render_post

urlpatterns = [
    path('', render_post, name = 'post'),
    # path('create_post/', create_post, name= 'create_post')
]
