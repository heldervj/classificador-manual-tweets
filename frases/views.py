from django.shortcuts import render, redirect
from frases.models import Tweet
import re
import random


# Create your views here.

def index(request):
    if request.method == 'POST':
        classificacao = re.search('classificacao=(.*)&', request.body.decode()).group(1)
        id = re.search('id=(.*)', request.body.decode()).group(1)
        print(classificacao)
        print(id)
        t = Tweet.objects.get(pk=id)
        t.primeira_avaliacao = classificacao
        t.save()
        return redirect('/frases')
    else:
        t = random.choice(Tweet.objects.all().filter(primeira_avaliacao=''))

        avaliados = len(Tweet.objects.all().exclude(primeira_avaliacao=''))
        total = len(Tweet.objects.all())

        context = {
            'id': t.id,
            'frase': t.text,
            'avaliados': avaliados,
            'total': total
        }

        return render(request, 'index.html', context)
