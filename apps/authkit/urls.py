from django.contrib import admin
from django.urls import path,include
from .views import RegisterView,LoginAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apps.authkit.urls')),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginAPIView.as_view(), name='login')
]
