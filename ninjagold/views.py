from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):

  if 'gold' not in request.session:
    request.session['gold'] = 0
  
  return render(request,'index.html')

def farm(request):

  request.session['gold'] += random.randint(10,20)
  return redirect('/')

def cave(request):

  request.session['gold'] += random.randint(5,10)
  return redirect('/')

def house(request):

  request.session['gold'] += random.randint(2,5)
  return redirect('/')

def casino(request):

  request.session['gold'] += random.randint(-50,50)
  return redirect('/')

def reset(request):
  
  request.session['gold'] = 0
  return redirect('/')

def success(request):
  return render(request, 'success.html')