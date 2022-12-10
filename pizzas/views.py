from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')



def menu(request):
    menu = Pizza.objects.all()
    context = {'all_pizzas':menu}
    return render(request, 'pizzas/menu.html', context)



def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    context = {'pizza':p, 'toppings':toppings}
    return render(request, 'pizzas/menu.html', context)

