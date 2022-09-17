from django.shortcuts import render
import requests # İstek gönderiyoruz =>axios 
from pprint import pprint
from .models import Coin

# Create your views here.

def home(request):
     coin=request.GET.get("coin_name")
     pprint(coin)
     url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
     response = requests.get(url)
     content = response.json()  # dict formatına çevirdik
     #pprint(content[0]["name"])



     for i in content:
        if i["name"] ==coin:
            name_c=i["name"]
            if Coin.objects.filter(name=name_c):
                continue

            else:
                Coin.objects.create(name=name_c)
        else:
            continue
            #girilen veri api de yok
                


     return render(request,"app/home.html")
     
