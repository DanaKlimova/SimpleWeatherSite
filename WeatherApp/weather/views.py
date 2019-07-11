from django.shortcuts import render
import requests

def index(request):
    appid = '42cc7376ff8fe1eaf19bb800bba4e8ba'
    city = 'London'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    response = requests.get(url.format(city)).json()  #get data in dictionary format

    city_info = {
    'city': city,
    'temp': response['main']['temp'],
    'icon': response['weather'][0]['icon']
    }

    context = {'info': city_info}
    return render(request, 'weather/index.html', context)
