from django.shortcuts import render
from django.http import HttpResponse
from cse.models import adm
from cse.forms import admForm
# Create your views here.
def think(request):
    return HttpResponse("teju")
def admissions(request):
    return HttpResponse("admissions for college.")
def firstpage(request):
    dic = {"name":"teju","branch":"ece"}
    return render(request,'cse/home.html',dic)
def dataview(request):
    a = adm.objects.all()
    dic = {'res':a}
    return render(request,'cse/viewing.html',dic)
def datainsert(request):
    form = admForm
    dic={'form':form}
    if request.method == 'POST':
        form=admForm(request.POST)
        if form.is_valid():
            form.save()
            return dataview(request)
        
    return render(request,'cse/dform.html',dic)

