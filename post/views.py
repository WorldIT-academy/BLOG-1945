from django.shortcuts import render
from .models import Post, Author, Tag
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
import colorama

colorama.init(autoreset= True)
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW

# Create your views here.
def render_post(request: HttpRequest):
    all_post = Post.objects.all()
    all_tags = Tag.objects.all()
    return render(
        request= request, 
        template_name= 'post/post.html',
        context= {
            "posts": all_post,
            "tags": all_tags
        }
    )

# @login_required
def create_post(request: HttpRequest):
    if request.method == "POST":
        print(1)
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.getlist('tags')
        
        print(f"{GREEN}title: {YELLOW}{title}\n{GREEN}content: {YELLOW}{content}\n{GREEN}tags: {YELLOW}{tags}")
    
    
