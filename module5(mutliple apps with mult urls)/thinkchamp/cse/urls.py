from django.urls import path
from cse.views import think
from cse.views import admissions
urlpatterns = [
    path('th/', think),
    path('ad/', admissions),
]
