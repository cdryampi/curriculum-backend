from django.db import models
from colorfield.fields import ColorField


class SingletonModel(models.Model):
    class Meta:
        abstract = True  # Esta clase es abstracta, no genera una tabla en la base de datos.

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise Exception(f'No se puede crear más de una instancia de {self.__class__.__name__}')
        return super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Tag(models.Model):
    
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre del Tag"
    )
    color = ColorField(
        default='#FF0000',
        verbose_name="Color",
        help_text="Escoge un color para el tag."
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nombre
