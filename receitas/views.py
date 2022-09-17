from rest_framework import generics
from receitas.models import Receita
from receitas.serializers import ReceitaSerializer


class ReceitaListView(generics.ListAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
