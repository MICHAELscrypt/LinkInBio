from django.urls import path
from .views import your_view, add_user_link

urlpatterns = [
    path('path/to/view/<str:username>/', your_view, name='your_view_name'),
    path('add/', add_user_link, name='add_userLink')
]
