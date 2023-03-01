

from django import forms

from .models import Barrio, Calle


class BarrioForm(forms.ModelForm):
    description = forms.Textarea()

    def __init__(self, *args, **kwargs):
        super(BarrioForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Barrio
        fields = ['descripcion']



class CalleForm(forms.ModelForm):
    description = forms.Textarea()

    def __init__(self, *args, **kwargs):
        super(CalleForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Calle
        fields = ['descripcion']
