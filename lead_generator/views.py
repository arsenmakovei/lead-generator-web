from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from lead_generator.forms import UserCreateForm, LeadGeneratorForm
from lead_generator.models import User


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class LeadGeneratorView(LoginRequiredMixin, View):
    def get(self, request):
        form = LeadGeneratorForm()
        return render(request, "lead_generator/lead_generator.html", {"form": form})

    def post(self, request):
        form = LeadGeneratorForm(request.POST)
        return render(request, "lead_generator/lead_generator.html", {"form": form})
