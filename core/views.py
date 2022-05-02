
from audioop import reverse
from re import template
from telnetlib import STATUS
from aiohttp import content_disposition_filename
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Search, Alvo
from .forms import SearchForm, AlvoForm
import folium
from django.contrib import messages
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    form = AlvoForm
    context = {
        'form' : form
    }
    mapa(request)
    return render(request, 'home.html', context)


def mapa(request):
    alvos = Alvo.objects.all()
    print(alvos)
    mapa = folium.Map(width=800, height=500,location=[10, 12], zoom_start=1)
    # print(folium.add_child() )
    for alvo in alvos:
        folium.Marker(location=[alvo.latitude, alvo.longitude],
        tooltip='Maguinho!', popup=f"<li class='nav-item dropdown'><a class='nav-link  active dropdown-toggle' href='#' id='navbarDropdown' role='button' data-bs-toggle='dropdown' aria-expanded='false'>Alvo</a>   <ul class='dropdown-menu' aria-labelledby='navbarDropdown'> <li><a class='dropdown-item' aria-current='page' data-bs-toggle='modal' data-bs-title='{{ alvo.nome}}'   data-bs-target='#deleteModal' data-bs-url ='delete-alvo/{alvo.id}'>Delete</a></li>   <li><a class='dropdown-item' aria-current='page'  data-bs-toggle='modal' data-bs-target='#editModal' data-bs-title='Adicionar Alvo' form='form' data-bs-url= 'editar-alvo/{alvo.id}'>Editar</a></li></ul></li>").add_to(mapa)




    mapa.save('core/templates/mapa.html')
    mapa.render()

    context = {
        'alvos' : alvos,
    } 

    return render(request, 'mapa.html', context)


def adicionar_alvo(request):
    form = AlvoForm(request.POST or None)
    print('a')
    if request.method == 'POST':
        print('b')
        if form.is_valid():
            print('c')
            alvo = form.save()
            data = [alvo.to_dict()]
            return HttpResponse('oiiiii')
    return HttpResponse('aa')


def edita_alvo(request, pk):
    template_name = 'form_alvo.html'
    request.method = 'POST'
    print(request.method)
    alvo = get_object_or_404(Alvo, pk=pk)
    form = AlvoForm(request.POST or None, instance=alvo)
    if request.method == 'POST':
        if form.is_valid():
            alvo = form.save()
            messages.success(request, 'Alvo Atualizado')
            return JsonResponse({'status' : 1, 'url' : reverse('home')}, status=200)
        else:
            context = {
                'form' : form,
            }
    context = {
        'alvo' : alvo,
        'form' : form,
    }
    return JsonResponse({'data': render_to_string(template_name, context)}, status=200)


def delete_alvo(request, pk):
    if request.method == "POST":
        alvo = get_object_or_404(Alvo, pk=pk)
        alvo.delete()
        messages.success(request, 'Alvo deletado com Sucesso!')
        return redirect(reverse('home'))
    

