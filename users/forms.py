from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Лично име", help_text="Използвайте истинското си име", max_length=255, required=True)
    last_name = forms.CharField(label="Фамилно име", help_text="Използвайте истинското си име", max_length=255, required=True)
    email = forms.EmailField(label="Електронна поща",help_text="Препоръчително е да се използва ученическата поща", required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")