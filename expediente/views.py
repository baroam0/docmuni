

from django.contrib import messages

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import ExpedienteForm
from .models import Expediente


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



# Create your views here.
