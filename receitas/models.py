from django.db import models


class Receita(models.Model):
    nome = models.CharField(max_length=255)
    decricao = models.TextField()
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=18)
    imagens = models.ImageField(blank=True)

    def __str__(self):
        return self.nome
