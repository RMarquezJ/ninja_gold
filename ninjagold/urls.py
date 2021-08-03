from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('reset', views.reset),
  path('success', views.success),
  path('earn/<place>', views.earn),
  # path('farm', views.farm),
  # path('cave', views.cave),
  # path('house', views.house),
  # path('casino', views.casino),
]