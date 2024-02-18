from django.urls import path
from .views import your_view, add_user_link

urlpatterns = [
    path('link/add/', add_user_link, name='add_userLink'),
    #path('link/edit/', add_user_link, name='add_userLink'),
    #path('user/edit/', add_user_link, name='add_userLink'),
    #path('user/editlinks/', add_user_link, name='add_userLink'),
    path('<str:username>/', your_view, name='your_view_name'),
]
