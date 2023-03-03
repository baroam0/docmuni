
from django import forms


from .models import Expediente, Estado, TipoExpediente, Obra, Certificado
from contratistas.models import Contratista
from locacion.models import Barrio, Calle


class ExpedienteForm(forms.ModelForm):
    nomenclatura = forms.CharField(label="Nomenclatura", required=True)    
    descripcion = forms.Textarea()
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

    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(), label="Estados")

    tipoexpediente = forms.ModelChoiceField(
        queryset=TipoExpediente.objects.all(), label="Tipo Expediente")

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


class ObraForm(forms.ModelForm):
    montooficial = forms.DecimalField(
        decimal_places=2,
        max_digits=10,
        label="Monto Adjudicadicado",
        required=False)

    montoadjudicado = forms.DecimalField(label="Monto Adjudicadicado", required=False)
    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.all().order_by("descripcion"),
        label="Contratista",
        required=False
    )

    numeroprocedimiento = forms.CharField(label="Numero de Procedimiento", required=True)
    decretoadjudicacion = forms.CharField(label="Decreto de Adjudicacion", required=True)

    def __init__(self, *args, **kwargs):
        super(ObraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Obra
        fields = [
            'montooficial', 'montoadjudicado', 'contratista',
            'numeroprocedimiento', 'decretoadjudicacion'
    ]



class ExpedienteCertificadoForm(forms.ModelForm):
    nomenclatura = forms.CharField(label="Nomenclatura", required=True)    
    descripcion = forms.Textarea()

    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(), label="Estados")

    tipoexpediente = forms.ModelChoiceField(
        queryset=TipoExpediente.objects.all(), label="Tipo Expediente")

    def __init__(self, *args, **kwargs):
        super(ExpedienteCertificadoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Expediente
        fields = ['nomenclatura', 'descripcion', 'tipoexpediente', 'estado']


class CertificadoForm(forms.ModelForm):    
    obra = forms.ModelChoiceField(
        queryset=Obra.objects.all().order_by("expediente"),
        label="Obra",
        required=False
    )
    montocertificado = forms.DecimalField(
        label="Monto Certificado", required=False)
    def __init__(self, *args, **kwargs):
        super(CertificadoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Certificado
        fields = [
            'obra', 'montocertificado'
    ]