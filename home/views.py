from django.shortcuts import render
from .models import Users

# Create your views here.
def render_home(request):

    all_users = Users.objects.all()
    
    return render(
        request= request, 
        template_name= 'home/home.html',
        context= {
            'title': 'Home Page',  # This will be rendered in the template as {{ title }}
            'user_name': all_users[0].name
        } 
    )
