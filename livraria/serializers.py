from livraria.models import Categoria, Livro, Editora, Autor
from rest_framework.serializers import ModelSerializer


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
