from django.urls import path

from lead_generator.views import UserCreateView, LeadGeneratorView

urlpatterns = [
    path("accounts/signup/", UserCreateView.as_view(), name="signup"),
    path("lead-generator/", LeadGeneratorView.as_view(), name="lead-generator"),
]

app_name = "lead_generator"
