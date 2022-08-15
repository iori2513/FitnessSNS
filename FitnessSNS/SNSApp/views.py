from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class SignUpView(generic.TemplateView):
    template_name = "sign-up.html"

class SignInView(generic.TemplateView):
    template_name: str = "sign-in.html"
    
