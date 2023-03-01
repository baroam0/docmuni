

from django import forms

from .models import Expediente, Estado, TipoExpediente

from locacion.models import Barrio, Calle


class ExpedienteForm(forms.ModelForm):
    
    #fecha = forms.CharField(label="Fecha de Registro", required=False)

    nomenclatura = forms.CharField(label="Nomenclatura", required=True)    
    descripcion = forms.CharField(label="Descripcion", required=False)
    observacion = forms.Textarea()
    
    barrio = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Barrio.objects.all().order_by("descripcion"),
        widget=forms.CheckboxSelectMultiple
    )

    calle = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Calle.objects.all().order_by("descripcion"),
        widget=forms.CheckboxSelectMultiple
    )

    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), label="Estados")
    tipoexpediente = forms.ModelChoiceField(queryset=TipoExpediente.objects.all(), label="TipoExpediente")

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            
            if field == "calle" or field == "barrio":
                self.fields[field].widget.attrs.update({
                    'class': 'i-checks'
                })
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

    class Meta:
        model = Expediente
        fields = ['nomenclatura', 'descripcion', 'observacion', 'tipoexpediente', 'estado', 
                  'fechaestado', 'barrio', 'calle']
