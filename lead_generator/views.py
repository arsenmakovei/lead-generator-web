from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from lead_generator.forms import UserCreateForm
from lead_generator.models import User


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
