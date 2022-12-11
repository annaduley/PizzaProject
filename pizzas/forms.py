from django import forms 
from .models import*

class toppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping_name']
        label = {'pizza_name':'Add a Comment'}