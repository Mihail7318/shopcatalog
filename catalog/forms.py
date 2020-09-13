from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserAccount
        fields = ("phone_number", "name", "surname", "patronymic",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ("phone_number", "name", "surname", "patronymic",)