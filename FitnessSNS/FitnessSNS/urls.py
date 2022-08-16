from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('SNSApp.urls')),
    path('accounts/', include('allauth.urls')),
]
