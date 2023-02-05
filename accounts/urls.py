from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/', dictionaryFindView.as_view(), name='dictionaryFind'),
]
