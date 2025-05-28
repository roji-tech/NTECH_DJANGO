from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth
# from accounts.views import CustomLoginView

urlpatterns = [
    path('', include('todo.urls')),
    path('blogs/', include('blog.urls')),
    path("shortner/", include("url_shorner.urls")),
    path('myadmin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
    path('auth/', include("accounts.urls")),
    path('api-auth/', include('rest_framework.urls'))
    # path('auth/login/', CustomLoginView.as_view(),)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
