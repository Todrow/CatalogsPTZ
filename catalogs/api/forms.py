from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class SignUpForm(UserCreationForm):
    ADMIN = "AD"
    USER = "US"
    CATALOG = "CG"
    ROLES_CHOICES = {
        ADMIN: "Admin",
        USER: "User",
        CATALOG: "Catalog",
    }
    email = forms.EmailField(
        max_length=254, help_text='Обязательное поле. Введите действующий email.')
    role = forms.ChoiceField(choices=ROLES_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
