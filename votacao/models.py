from __future__ import unicode_literals



# Create your models here.

from django.db import models


class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data de publicação')

    def __str__(self):
        return self.pergunta_texto


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.resposta_texto

    def votar(self):
        self.votos += 1
