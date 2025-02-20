from django import forms
from cse.models import adm
class admForm(forms.ModelForm):
    class Meta:
        model = adm
        fields = '__all__'
class venderForm(forms.Form):
    name =forms.CharField(max_length=1000)
    age = forms.IntegerField()
