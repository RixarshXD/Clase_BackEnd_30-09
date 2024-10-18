from django import forms
from APP1.models import Proyecto


class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'