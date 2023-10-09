from django.shortcuts import render
import requests

def home(request):
    api_key = "5d007cae548981e870429797d5dc380a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city = "Trois-Rivieres"  # ou n'importe quelle autre ville
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != 404:  # Si la requête a réussi
        main_data = data["main"]
        weather_data = {
            "city": city,
            "country": data["sys"]["country"],
            "temperature": main_data["temp"],
            "description": data["weather"][0]["description"],
        }
    else:
        weather_data = {}

    return render(request, "home.html", {"weather_data": weather_data})


from django.http import JsonResponse

def get_weather_data(request):
    city = request.GET.get('city', 'Paris')
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "5d007cae548981e870429797d5dc380a"  # votre clé API
    api_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(api_url)
    if response.status_code != 200:
        # Si l'API externe renvoie une erreur, renvoyez une erreur JSON avec le statut HTTP et le message d'erreur
        return JsonResponse({'error': f"API returned {response.status_code}: {response.text}"}, status=response.status_code)
    
    data = response.json()
    
    return JsonResponse({
        'temperature': data['main']['temp'],
        'city': data['name'],
        # ... autres données que vous souhaitez extraire ...
    })
