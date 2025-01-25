from django.shortcuts import render
from .models import Post, Author
# Create your views here.
def render_post(request):
    all_post = Post.objects.all()
    return render(
        request= request, 
        template_name= 'post/post.html',
        context= {
            "posts": all_post
        }
    )