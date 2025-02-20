from django.urls import path
from ece.views import college
urlpatterns = [
    path('clg/', college),
]
