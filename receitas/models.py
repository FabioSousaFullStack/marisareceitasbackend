from django.db import models


class Receita(models.Model):
    nome = models.CharField(max_length=255)
    breve_descricao = models.TextField()
    link_do_video = models.URLField(max_length=300)

    def __str__(self):
        return self.nome
