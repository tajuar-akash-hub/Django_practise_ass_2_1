from django.shortcuts import render
from django.http import HttpResponse
from. forms import ContactForm
import datetime

from . import forms


def home(request):
    return HttpResponse("welcome to homepage")

# Create your views here.
def form(request):
    today_day = datetime.date.today()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'./form.html',{'form':form,'datetime':today_day})
    else:
        form=ContactForm()       
        return render(request,"./form.html",{'form':form,'datetime':today_day})
    


    
    
    


    
            
    

