import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Pizzeria.settings')

import django
django.setup()

from pizzas.models import Pizza
from pizzas.models import Topping

pizza = Pizza.objects.all()
topping =  Topping.objects.all()



for t in pizza:
    print(t)
    print(t.pizza_name)

w = Pizza.objects.get(id=1)
print(w)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username)
    print(user.last_login)
