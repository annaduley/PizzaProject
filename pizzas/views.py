from django.shortcuts import render, redirect
from .models import *
import base64
from .forms import*

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')



def menu(request):
    menu = Pizza.objects.all()
    context = {'all_pizzas':menu}
    return render(request, 'pizzas/menu.html', context)



def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    topping_name = Topping.objects.filter(pizza=p)
    if (pizza_id == 1):
        link = 'https://www.spam.com/wp-content/uploads/2019/09/image-recipe_spam-hawaiian-pizza-1000x500.jpg'
    elif (pizza_id == 2):
        link = 'https://www.pizzahut.com/c/assets/img/meat-lovers-pizza_875x300.jpg'
    elif (pizza_id == 3):
        link = 'https://www.foodandwine.com/thmb/Wd4lBRZz3X_8qBr69UOu2m7I2iw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-cheese-pizza-FT-RECIPE0422-31a2c938fc2546c9a07b7011658cfd05.jpg'
    elif (pizza_id == 4):
        link = 'https://cdn.tasteatlas.com/images/dishes/b05a0af72ad845f3a6abe16143d7853a.jpg?mw=1300'
    else:
        link = 'https://www.tasteandtellblog.com/wp-content/uploads/2021/01/BBQ-Chicken-Pizza-3.jpg'
    context = {'pizza':p, 'topping_name':topping_name, 'link':link}
  
    return render(request, 'pizzas/pizza.html', context)

def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = toppingForm()
    else:
        print(request.POST)
        form = toppingForm(data=request.POST)
        if form.is_valid():
            newComment = form.save(commit = False)
            newComment.pizza = pizza
            newComment.save()
            return redirect('pizzas:pizza', pizza_id = pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/comment.html', context)
