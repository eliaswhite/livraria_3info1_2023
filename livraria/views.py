from livraria.serializers import (
    CategoriaSerializer,
    EditoraSerializer,
    AutorSerializer,
    LivroSerializer,
)
from livraria.models import Livro, Categoria, Autor, Editora
from rest_framework.viewsets import ModelViewSet


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
