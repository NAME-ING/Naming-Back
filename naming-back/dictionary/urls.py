from django.urls import path
from .views import *

app_name = 'dictionary'

urlpatterns = [
    path('', dictionaryMakeView.as_view()),
    path('<int:pk>/', dictionaryView.as_view()),
    path('<int:pk>/post/', postListView.as_view()),
    path('<int:pk>/post/<int:post_pk>', postDeleteView.as_view()),
]