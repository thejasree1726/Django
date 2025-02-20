from django import forms
from cse.models import adm
class admForm(forms.ModelForm):
    class Meta:
        model = adm
        fields = '__all__'