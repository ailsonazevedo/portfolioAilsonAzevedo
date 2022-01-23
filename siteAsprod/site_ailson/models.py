from django.db import models


class Projeto(models.Model):
  nome = models.CharField(max_length=250)
  descricao = models.CharField(max_length=250)
  foto_projeto = models.FileField(upload_to="media/", null=True)
  
  def __str__(self):
    return self.nome
