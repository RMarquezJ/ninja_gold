from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):

  if 'gold' not in request.session:
    request.session['gold'] = 0

  if 'log' not in request.session:
    request.session['log'] = []
  
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

  request.session['color'] = 'white'

  if rand >= 0:

    request.session['log'].insert(0, f'Earned {rand} gold from {place} ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})')
    request.session['color'] = 'success'

  else:

    request.session['log'].insert(0, f'Lost {-rand} gold from {place} ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})')
    request.session['color'] = 'danger'
  
  return redirect ('/success')

def reset(request):
  
  request.session['gold'] = 0
  request.session['log'] = []

  return redirect('/success')

def success(request):

  return render(request, 'play.html')