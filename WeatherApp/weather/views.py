from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City


def index(request):
    appid = '42cc7376ff8fe1eaf19bb800bba4e8ba'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm() # нужно для отчистки формочки

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()  #get data in dictionary format
        city_info = {
        'city': city.name,
        'temp': response['main']['temp'],
        'icon': response['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
