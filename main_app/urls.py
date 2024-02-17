from django.urls import path
from .views import your_view

urlpatterns = [
    path('path/to/view/<str:username>/', your_view, name='your_view_name'),
]
