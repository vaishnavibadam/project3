# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse
from .models import Person
from django.shortcuts import render
from .forms import NameForm
# Create your views here.
def index(request):
 all_values=Person.objects.all()
 context={'all_values':all_values}
 if request.method == 'POST':

   form = NameForm(request.POST)

   if form.is_valid():
     obj=Person()
     obj.first_name=form.cleaned_data['first_name']
     obj.last_name=form.cleaned_data['last_name']
     obj.save()
     #return HttpResponseRedirect('/thanks/')  
 else:
     form=NameForm()
 return render(request,'index.html',{'form':form,'all_values':all_values})    
 #return render(request,'index.html',context)
def thanks(request):
  return HttpResponse('Thank You')
  
