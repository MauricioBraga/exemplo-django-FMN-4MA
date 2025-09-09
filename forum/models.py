from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200, null = False)
    detalhe = models.TextField(null = False)
    tentativa = models.TextField()
    data_criacao = models.DateTimeField('criado em ')
    usuario = models.CharField(max_length=200, null = False, default="anônimo")

    def foi_publicado_recentemente(self):
        now = timezone.now()
        return self.data_criacao >= now - timezone.timedelta(days=1)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.titulo
    
class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField(null = False)
    data_criacao = models.DateTimeField('criado em ')
    usuario = models.CharField(max_length=200, null = False, default="anônimo")

    def __str__(self):
        return "[" + str(self.id) + "] " + self.texto
    
    def foi_publicado_recentemente(self):
        now = timezone.now()
        return self.data_criacao >= now - timezone.timedelta(days=1)
    
