
from django.forms.widgets import NumberInput
import datetime
from django import forms

favorite_color= [('blue','blue'),
                 ('white','white'),
                 ('black','black')]

class ContactForm(forms.Form):
    name = forms.CharField( initial="Tajuar Akash",max_length=20, required=False)
    email = forms.EmailField(label="Please enter your email address",required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField()
    dateInput= forms.DateField(initial=datetime.date.today,label="Enter Date",widget=NumberInput(attrs={'type':'date'}))
    favorite_color =forms.ChoiceField(label="Enter your favorite color" ,choices=favorite_color, required=False)




