from django.contrib.auth.forms import UserCreationForm
from .models import accounts

class RegisterForm(UserCreationForm):
    class Mete:
        model = accounts
        fields = ['email']