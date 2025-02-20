from django.urls import path
from cse.views import think
from cse.views import admissions
from cse.views import firstpage,dataview,datainsert
urlpatterns = [
    path('th/', think),
    path('ad/', admissions),
    path('fp/', firstpage),
    path('result/', dataview),
    path('dataform/',datainsert),
]
