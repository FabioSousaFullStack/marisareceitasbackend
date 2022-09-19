from django.db import models


class Receita(models.Model):
    nome = models.CharField(max_length=255)
    breve_descricao = models.TextField()
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=18)
    link_imagens = models.URLField(max_length=300)

    def __str__(self):
        return self.nome
