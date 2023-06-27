from django.contrib.auth.forms import UserCreationForm
from django import forms

from lead_generator.models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)
