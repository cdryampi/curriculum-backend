from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .utils import validate_image_file

class MediaFile(models.Model):
    """
        Clase que representar a un fichero de una imagen.
    """
    file = models.FileField(
        upload_to='media_files/',
        validators= [validate_image_file]
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Título",
        help_text="Título o descripción de la imagen."
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Versiones de imagen redimensionadas para diferentes dispositivos
    image_for_pc = ImageSpecField(
        source='file',
        processors=[ResizeToFill(1920, 1080)],
        format='JPEG',
        options={'quality': 90}
    )
    image_for_tablet = ImageSpecField(
        source='file',
        processors=[ResizeToFill(1024, 768)],
        format='JPEG',
        options={'quality': 90}
    )
    image_for_mobile = ImageSpecField(
        source='file',
        processors=[ResizeToFill(640, 480)],
        format='JPEG',
        options={'quality': 90}
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Media File {self.file.name}"

class DocumentFile(models.Model):
    """
        Clase que representa a un fichero para el CV.
    """
    title = models.CharField(
        max_length=255,
        verbose_name="Título del Documento"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Carga"
    )
    file = models.FileField(
        upload_to='documents/',
        verbose_name="Archivo",
        help_text="Suba un archivo PDF."
    )

    class Meta:
        verbose_name = "Archivo de Documento"
        verbose_name_plural = "Archivos de Documentos"

    def __str__(self):
        return f"{self.title} ({self.uploaded_at.strftime('%Y-%m-%d')})"
