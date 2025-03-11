from PIL import Image
import os
from django.conf import settings

def generate_images_task(media_file_id):
    """
    Genera versiones redimensionadas de la imagen y las asigna al modelo.
    """
    from multimedia_manager.models import MediaFile  # Evitar importaciones circulares

    try:
        media_file = MediaFile.objects.get(id=media_file_id)

        # Verificar si ya existen las imágenes
        if media_file.image_for_pc and media_file.image_for_tablet and media_file.image_for_mobile:
            return f"Las imágenes ya están generadas para {media_file_id}"

        # Eliminar versiones anteriores si existen
        eliminar_imagenes_de_cache(media_file)

        file_path = media_file.file.path  # Ruta de la imagen original
        img = Image.open(file_path)

        sizes = {
            'pc': (1920, 1080),
            'tablet': (1024, 768),
            'mobile': (480, 320)
        }

        for key, size in sizes.items():
            new_dir = os.path.join(settings.MEDIA_ROOT, key)
            os.makedirs(new_dir, exist_ok=True)

            new_path = os.path.join(new_dir, os.path.basename(file_path))

            img_resized = img.resize(size, Image.LANCZOS)
            img_resized.save(new_path, format="JPEG", quality=90)

            setattr(media_file, f"image_for_{key}", f"{key}/{os.path.basename(file_path)}")

        media_file.save()
        return f"✅ Imágenes generadas para {media_file_id}"

    except MediaFile.DoesNotExist:
        return f"❌ Error: No se encontró la imagen con ID {media_file_id}"


def eliminar_imagenes_de_cache(media_file):
    """
    Elimina los archivos en caché antes de regenerar imágenes.
    """
    paths = [
        media_file.image_for_pc,
        media_file.image_for_tablet,
        media_file.image_for_mobile
    ]

    for path in paths:
        if path and os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
            os.remove(os.path.join(settings.MEDIA_ROOT, path))
