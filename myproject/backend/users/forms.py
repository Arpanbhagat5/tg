import re

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Pref


class CustomUserCreationForm(UserCreationForm):
    tel = forms.CharField(required=False, max_length=20)
    pref = forms.ChoiceField(
        choices=Pref.PrefChoices.choices, required=False
    )  # Updated field

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "tel", "pref"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if (
            len(password) < 8
            or not re.search(r"[A-Z]", password)
            or not re.search(r"[a-z]", password)
            or not re.search(r"\d", password)
        ):
            raise forms.ValidationError(
                "Password must be at least 8 characters, including an uppercase letter, lowercase letter, and a number."
            )
        return password

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        if tel and not re.match(r"^\d+$", tel):
            raise forms.ValidationError("Phone number must contain only digits.")
        return tel

    def clean_pref(self):
        pref = self.cleaned_data.get("pref")
        if pref:
            # Fetch the Pref instance corresponding to the name
            try:
                pref_instance = Pref.objects.get(name=pref)
            except Pref.DoesNotExist:
                raise forms.ValidationError("Invalid prefecture selected.")
            return pref_instance
        return None

    def save(self, commit=True):
        user = super().save(commit=False)
        pref_instance = self.clean_pref()
        if pref_instance:
            user.pref = pref_instance  # Set the Pref instance
        if commit:
            user.save()
        return user
