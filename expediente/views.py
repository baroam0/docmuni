

from django.contrib import messages

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CertificadoForm, ExpedienteForm, ObraForm, ExpedienteCertificadoForm
from .models import Expediente, Obra, Certificado
from contratistas.models import Contratista



def expedientelist(request):
    queryresults = Expediente.objects.all().order_by('descripcion')
    paginador = Paginator(queryresults, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    results = paginador.get_page(page)
    return render(request, 'expediente/expediente_list.html', {'results': results})


def expedientenew(request):
    if request.POST:
        form = ExpedienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO EL EXPEDIENTE")
            return redirect('/expediente/expedientelist')
        else:
            return render(request, 'expediente/expediente_edit.html', {"form": form})
    else:
        form = ExpedienteForm()
        return render(request, 'expediente/expediente_edit.html', {"form": form})


def expedienteedit(request, pk):
    query = Expediente.objects.get(pk=pk)

    if request.POST:
        form = ExpedienteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO EL EXPEDIENTE.")
            return redirect('/expediente/expedientelist')
        else:
            return render(request, 'expediente/expediente_edit.html', {"form": form})
    else:
        form = ExpedienteForm(instance=query)
        return render(request, 'expediente/expediente_edit.html', {"form": form})


def obralist(request):
    queryresults = Obra.objects.all().order_by('pk')
    paginador = Paginator(queryresults, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    results = paginador.get_page(page)
    return render(request, 'expediente/obra_list.html', {'results': results})


def obranew(request):
    if request.POST:
        formexpediente = ExpedienteForm(request.POST)
        formobra = ObraForm(request.POST)

        if formexpediente.is_valid() and formobra.is_valid():
            formexpediente.save()
            contratista = Contratista.objects.get(id=request.POST.get('contratista'))
            nomenclatura = Expediente.objects.get(nomenclatura=request.POST.get('nomenclatura'))

            obra = Obra(
                expediente=nomenclatura,
                montoadjudicado=request.POST.get("montoadjudicado"),
                montooficial=request.POST.get("montooficial"),
                contratista=contratista,
            )

            obra.save()
            messages.success(request, "SE HA GRABADO LA OBRA")
            return redirect('/expediente/obralist')
        else:
            return render(
                request,
                'expediente/obra_edit.html',
                {
                    "formexpediente": formexpediente,
                    "formobra": formobra
                })
    else:
        formexpediente = ExpedienteForm()
        formobra = ObraForm()
        return render(
            request,
            'expediente/obra_edit.html',
            {
                "formexpediente": formexpediente,
                "formobra": formobra
            })


def obraedit(request, pk):
    obra = Obra.objects.get(pk=pk)
    expediente = Expediente.objects.get(pk=obra.expediente.pk)

    if request.POST:
        formexpediente = ExpedienteForm(request.POST, instance=expediente)
        formobra = ObraForm(request.POST, instance=obra)
        if formexpediente.is_valid() and formobra.is_valid():
            formexpediente.save()
            formobra.save()
            messages.success(request, "SE HA ACTUALIZADO EL EXPEDIENTE.")
            return redirect('/expediente/obralist')
        else:
            return render(
                request,
                'expediente/obra_edit.html',
                {
                    "formexpediente": formexpediente,
                    "formobra": formobra
                })
    else:
        formobra = ObraForm(instance=obra)
        formexpediente = ExpedienteForm(instance=expediente)
        return render(
            request,
            'expediente/obra_edit.html',
            {
                "formexpediente": formexpediente,
                "formobra": formobra
            })


def certificadolist(request):
    queryresults = Certificado.objects.all().order_by('pk')
    paginador = Paginator(queryresults, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    results = paginador.get_page(page)
    return render(request, 'expediente/certificado_list.html', {'results': results})


def certificadonew(request):
    if request.POST:
        formexpedientecertificado = ExpedienteCertificadoForm(request.POST)
        formcertificado = CertificadoForm(request.POST)

        if formexpedientecertificado.is_valid() and formcertificado.is_valid():
            formexpedientecertificado.save()

            expediente = Expediente.objects.get(nomenclatura=request.POST.get("nomenclatura"))
            obra = Obra.objects.get(pk=request.POST.get("obra"))
            
            certificado = Certificado(
                expediente=expediente,
                obra=obra,
                montocertificado=request.POST.get("montocertificado"),
            )

            certificado.save()

            messages.success(request, "SE HA GRABADO EL CERTIFICADO")
            return redirect('/expediente/certificadolist')
        else:
            formexpedientecertificado = ExpedienteCertificadoForm(request.POST)
            formcertificado = CertificadoForm(request.POST)
            return render(
                request,
                'expediente/certificado_edit.html',
                {
                    "formexpedientecertificado": formexpedientecertificado,
                    "formcertificado": formcertificado
                })
    else:
        formexpedientecertificado = ExpedienteCertificadoForm
        formcertificado = CertificadoForm
        
        return render(
            request,
            'expediente/certificado_edit.html',
            {
                "formexpedientecertificado": formexpedientecertificado,
                "formcertificado": formcertificado
            })


def certificadoedit(request, pk):
    expediente = Expediente.objects.get(pk=pk)
    certificado = Certificado.objects.get(expediente=expediente)

    if request.POST:
        formexpedientecertificado = ExpedienteCertificadoForm(request.POST, instance=expediente)
        formobra = ObraForm(request.POST, instance=query)
        if formexpedientecertificado.is_valid():
            formexpedientecertificado.save()
            messages.success(request, "SE HA ACTUALIZADO EL CERTIFICADO.")
            return redirect('/expediente/certificadolist')
        else:
            return render(
                request,
                'expediente/certificado_edit.html',
                {
                    "formexpediente": formexpedientecertificado,
                    "formcertificado": formcertificado
                })
    else:

        formexpedientecertificado = ExpedienteCertificadoForm(instance=expediente)
        formcertificado = CertificadoForm(instance = certificado)

        return render(
            request,
            'expediente/certificado_edit.html',
            {
                "formexpedientecertificado": formexpedientecertificado,
                "formcertificado": formcertificado
            })

# Create your views here.
