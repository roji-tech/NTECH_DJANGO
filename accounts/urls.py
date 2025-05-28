from django.urls import include, path

from .views import RegistrationView, UserAPIView, UserModelViewSet, UsersList, get_users, users
from rest_framework.routers import DefaultRouter

app_name = "url_shorner"

router = DefaultRouter()
router.register(r'users', UserModelViewSet)


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('__users/', UsersList.as_view(), name='users'),
    path('myusers/', users, name='myusers'),
    path('api/', get_users, name='myusers'),
    path('api/users/', UserAPIView.as_view(), name='myusers2'),
    
    path('', include(router.urls)),
] 
# + router.urls
# {
#         "username": "test",
#         "email": "tes@domain.com",
#         "first_name": "Tester",
#         "last_name": "testing",
#         "password": "ZAQ!@WSX"
# }