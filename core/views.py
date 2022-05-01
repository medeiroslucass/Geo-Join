from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    # Create map objects
    # location recebe latitude e longitude (coordenadas)
    m = folium.Map(location=[33, 62], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Clique para mais', popup=country).add_to(m)
    
    # Get HTML representation
    m = m._repr_html_()
    context = {
        'm' : m,
        'form' : form

    }
    return render(request, 'index.html', context)