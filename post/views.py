from django.shortcuts import render
from .models import Post, Author, Tag
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .forms import PostForm
import colorama

colorama.init(autoreset= True)
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW

# Create your views here.

def render_post(request: HttpRequest):
    all_post = Post.objects.all()
    all_tags = Tag.objects.all()
    form = PostForm()
    if request.method == "POST":
    
        form_post = PostForm(request.POST, request.FILES)
        if form_post.is_valid():
            title = form_post.cleaned_data.get('title')
            content = form_post.cleaned_data.get('content')
            image = form_post.cleaned_data.get('image')
            
        
            print(f"{GREEN}title: {YELLOW}{title}\n{GREEN}content: {YELLOW}{content}")

    return render(
        request= request, 
        template_name= 'post/post.html',
        context= {
            "posts": all_post,
            "tags": all_tags,
            "form": form
        }
    )

    
