
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('auth/',include('user_auth.urls')),
    path('exam/',include('exam_app.urls')),
]
