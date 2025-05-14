from todo.views import home, index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('h/', home, name='home'),
]
