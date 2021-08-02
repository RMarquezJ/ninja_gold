from django.shortcuts import render, redirect, HttpResponse

def index(request):

  if 'gold' not in request.session:
    request.session['gold'] = 0
  
  return render(request,'index.html')


