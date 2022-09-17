from django.shortcuts import render
import requests # İstek gönderiyoruz =>axios 

# Create your views here.

def home(request):
     url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
     response = requests.get(url)
     content = response.json()
     print(content)

     return render(request,"app/home.html")
     
