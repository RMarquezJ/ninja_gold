from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):

  if 'gold' not in request.session:
    request.session['gold'] = 0
  
  return render(request,'index.html')

def earn(request, place):
  
  miin = None
  maax = None

  if place == 'farm':
    miin = 10
    maax = 20
  
  elif place == 'cave':
    miin = 5
    maax = 10

  elif place == 'house':
    miin = 2
    maax = 5

  elif place == 'casino':
    miin = -50
    maax = 50

  rand = random.randint(miin,maax)
  
  request.session['gold'] += rand
  
  return redirect ('/success')

def reset(request):
  
  request.session['gold'] = 0
  return redirect('/success')

def success(request):
  return render(request, 'play.html')

# def farm(request):

#   request.session['gold'] += random.randint(10,20)
#   return redirect('/success')

# def cave(request):

#   request.session['gold'] += random.randint(5,10)
#   return redirect('/success')

# def house(request):

#   request.session['gold'] += random.randint(2,5)
#   return redirect('/success')

# def casino(request):

#   request.session['gold'] += random.randint(-50,50)
#   return redirect('/success')