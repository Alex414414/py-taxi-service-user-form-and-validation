from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from taxi.models import Car


User = get_user_model()


class DriverCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("license_number",)


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("license_number",)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
