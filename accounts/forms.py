from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        pass



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        pass