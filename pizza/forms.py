from django import forms 


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='First Topping',max_length=100)
    topping2 = forms.CharField(label='Second Topping',max_length=100)
    size= forms.ChoiceField(label="Size",choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
