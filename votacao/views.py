from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Pergunta

def index(request):
    lista_recentes = Pergunta.objects.order_by('-pub_data')[:5]
    context = {'lista_recentes': lista_recentes}
    return render(request,'votacao/index.html',context)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request,'votacao/detalhes.html',{'pergunta':pergunta})

def resultado(request, pergunta_id):
    response = "Você está observando o resultado da pergunta %s."
    return HttpResponse(response % pergunta_id)

def voto(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'votacao/voto.html', {'pergunta': pergunta})