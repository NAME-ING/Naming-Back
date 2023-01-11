from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
]
