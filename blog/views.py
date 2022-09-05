from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.


# 4cc0a10b
# 5bdfee81719020965a984b95a247a86e	


def index(request):
    query="cheesecake"
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query+"&app_id=4cc0a10b&app_key=5bdfee81719020965a984b95a247a86e")
    jsonResponse = response.json()
    recipes = jsonResponse['hits']
    return render(request, 'blog/index.html', {'recipes': recipes})

def specific(request):
    return HttpResponse("This is the specific url")

