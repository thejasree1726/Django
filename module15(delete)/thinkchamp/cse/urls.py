from django.urls import path
from cse.views import think
from cse.views import admissions
from cse.views import firstpage,dataview,datainsert,vform,deleteAdm
urlpatterns = [
    path('th/', think),
    path('ad/', admissions),
    path('fp/', firstpage),
    path('result/', dataview),
    path('dataform/',datainsert),
    path('vender/',vform),
    path('delete/<int:id>',deleteAdm),
]
