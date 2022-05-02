
from audioop import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Search, Alvo
from .forms import SearchForm, AlvoForm
import folium
from django.contrib import messages

# Create your views here.
def home(request):
    form = AlvoForm

    context = {
        'form' : form
    }
    return render(request, 'home.html', context)


def mapa(request):
    alvos = Alvo.objects.all()
    print(alvos)
    mapa = folium.Map(width=800, height=500,location=[33, 62], zoom_start=0)
    for alvo in alvos:
        folium.Marker(location=[alvo.latitude, alvo.longitude],
        tooltip='Clique para saber mais!', popup=alvo.nome + '<a href="list/"><button class="botao">Ver</button></a>' + '<a href="add_alvo"><button class="botao"> Adicionar Alvo</button></a>').add_to(mapa)
    mapa.save('core/templates/mapa.html')

    context = {
        'alvos' : alvos,
    } 


    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = SearchForm()
    # address = Search.objects.all().last()
    # location = geocoder.osm(address)
    # lat = location.lat
    # lng = location.lng
    # country = location.country
    # if lat == None or lng == None:
    #     address.delete()
    #     return HttpResponse('You address input is invalid')
    # # Create map objects
    # # location recebe latitude e longitude (coordenadas)
    # m = folium.Map(location=[33, 62], zoom_start=2)
    # folium.Marker([lat, lng], tooltip='Clique para mais', popup=country).add_to(m)
    
    # # Get HTML representation
    # m = m._repr_html_()
    # context = {
    #     'm' : m,
    #     'form' : form

    # }
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
            return JsonResponse({'data' : data})
    return HttpResponse('aa')
