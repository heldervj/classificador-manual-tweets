from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:tweet_id>/salva/<classificacao>', views.salva_objeto, name='salva')
]