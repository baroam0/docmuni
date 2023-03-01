
from django.contrib import messages

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import BarrioForm, CalleForm
from .models import Barrio, Calle


def barriolist(request):
    queryresults = Barrio.objects.all().order_by('descripcion')
    paginador = Paginator(queryresults, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    results = paginador.get_page(page)
    return render(request, 'locacion/barrio_list.html', {'results': results})


def barrionew(request):
    if request.POST:
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO")
            return redirect('/locacion/barriolist')
        else:
            return render(request, 'locacion/barrio_edit.html', {"form": form})
    else:
        form = BarrioForm()
        return render(request, 'locacion/barrio_edit.html', {"form": form})


def barrioedit(request, pk):
    query = Barrio.objects.get(pk=pk)

    if request.POST:
        form = BarrioForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO EL BARRIO.")
            return redirect('/locacion/barriolist')
        else:
            return render(request, 'locacion/barrio_edit.html', {"form": form})
    else:
        form = BarrioForm(instance=query)
        return render(request, 'locacion/barrio_edit.html', {"form": form})


def callelist(request):
    queryresults = Calle.objects.all().order_by('descripcion')
    paginador = Paginator(queryresults, 10)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1

    results = paginador.get_page(page)
    return render(request, 'locacion/calle_list.html', {'results': results})



def callenew(request):
    if request.POST:
        form = CalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA GRABADO LA CALLE")
            return redirect('/locacion/callelist')
        else:
            return render(request, 'locacion/calle_edit.html', {"form": form})
    else:
        form = CalleForm()
        return render(request, 'locacion/calle_edit.html', {"form": form})



def calleedit(request, pk):
    query = Calle.objects.get(pk=pk)

    if request.POST:
        form = CalleForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA ACTUALIZADO LA CALLE.")
            return redirect('/locacion/callelist')
        else:
            return render(request, 'locacion/calle_edit.html', {"form": form})
    else:
        form = CalleForm(instance=query)
        return render(request, 'locacion/calle_edit.html', {"form": form})


# Create your views here.
