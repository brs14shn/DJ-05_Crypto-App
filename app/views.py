from django.shortcuts import render, redirect,get_object_or_404
import requests
from pprint import pprint
from .models import Coin

from django.contrib import messages

# Create your views here.

def home(request):
     coin=request.GET.get("coin_name") 
     pprint(coin)
     url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
     response = requests.get(url)
     content = response.json()  # dict formatına çevirdik
     #pprint(content[0]["name"])


    #  if coin:
    #     url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    #     response = requests.get(url)
    #     if response.ok:
    #          content = response.json()
    #          for i in content:
    #             if i["name"].lower() ==coin.lower():
    #                 name_c=i["name"]
    #                 if Coin.objects.filter(name=name_c):
    #                     messages.warning(request, "Coin already exists!")
                        
                        
    #                 else:
    #                     Coin.objects.create(name=name_c)
    #                     messages.success(request, 'City added!')
                        
                
    #             else:     
    #                 messages.warning(request, "There is no coin")  
    #                 coin=""
                   
                    

     if coin:
        for i in content:
            if i["name"].lower() ==coin.lower():
                name_c=i["name"]
                if Coin.objects.filter(name=name_c):
                    continue
                    #messages.warning(request, "Coin already exists!")
                else:
                    Coin.objects.create(name=name_c)
                    messages.success(request, 'City added!')
                     

            else:
                text="There is no coin"
                #messages.warning(request,text ) 
            #girilen veri api de yok
#*  ==================================
     coin_data=[]
     coins=Coin.objects.all().order_by("-id")

     for k in coins:
        #print(k)
        for n in content:
            if n["name"]==str(k):
                data={
                    "k":k,
                    "name":n["name"],
                    "image":n["image"],
                    "market":n["current_price"],    
                    "change":n["price_change_24h"]
                }
                #pprint(data)
                coin_data.append(data)
     context={
        "coin_data":coin_data
    }
      
                


     return render(request,"app/home.html",context)


def delete_coin(request, id):
    coin = get_object_or_404(Coin, id=id)
    coin.delete()
    messages.warning(request, 'City deleted!')
    return redirect('home')
     
