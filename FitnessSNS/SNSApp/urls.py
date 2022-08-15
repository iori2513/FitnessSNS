from django.urls import path

from . import views

app_name = 'SNSApp'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('signin/', views.SignInView.as_view(), name="signin"),
]