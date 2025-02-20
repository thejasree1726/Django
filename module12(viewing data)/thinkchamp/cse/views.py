from django.shortcuts import render
from django.http import HttpResponse
from cse.models import adm
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
