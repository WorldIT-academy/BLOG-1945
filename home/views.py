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
                'user_name': all_users[0] if all_users else 'Не знайдено'
            } 
        )
    # try:
    #     return render(
    #         request= request, 
    #         template_name= 'home/home.html',
    #         context= {
    #             'title': 'Home Page',  # This will be rendered in the template as {{ title }}
    #             # 'user_name': all_users[0] if all_users else 'Не знайдено'
    #             'user_name': all_users[0]
    #         } 
    #     )
    # except Exception as exception:
    #     print(f'An error occurred: {exception}')
    #     return render(
    #         request= request, 
    #         template_name= 'home/home.html',
    #         context= {
    #             'title': 'Home Page',
    #             'user_name': 'Не знайдено'
    #         } 
    #     )


# if all_users:
#     return all_users[0]
# else:
#     return None