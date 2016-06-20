from django.db import models


SafeDeleteMixin = safedelete_mixin_factory(HARD_DELETE_NOCASCADE)


class Categoria(SafeDeleteMixin):
    nombre = models.CharField(max_length=100)


class Producto(SafeDeleteMixin):
    nombre = models.CharField(max_length=100)
    categoria = models.ManyToManyField(Categoria)
