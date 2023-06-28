from django.contrib.auth.forms import UserCreationForm
from django import forms

from lead_generator.models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class LeadGeneratorForm(forms.Form):
    keywords = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Example: Restaurant, Hotel"}),
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Example: Boston"}),
    )
    leads_num = forms.ChoiceField(choices=[(x, x) for x in range(10, 101, 10)], initial=50)
