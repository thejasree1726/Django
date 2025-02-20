from django.shortcuts import render
from django.http import HttpResponse
from cse.models import adm
from cse.forms import admForm,venderForm
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
def  vform(request):
    form=venderForm
    dic={"form":form}
    if request.method=="POST":
        form = venderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['age'])
        return dataview(request)
    return render(request,"cse/vdform.html",dic)
def deleteAdm(request,id):
    a=adm.objects.get(id=id)
    a.delete()
    return dataview(request)

