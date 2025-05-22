from rest_framework import serializers
from .models import MediaFile, DocumentFile
from cv_backend.settings import URL_SERVER

class DocumentFileSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = DocumentFile
        fields = ['title', 'file', 'pdf_url']

    def get_url(self, obj, file_attr):
        """
            Método que devuelve la URL del archivo PDF.
            Si el archivo no existe, devuelve None.
        """
        request = self.context.get('request')
        file_attr = getattr(obj, 'file', None)
        if file_attr and hasattr(file_attr, 'url'):
            # Verifica si el archivo tiene una URL
            return request.build_absolute_uri(file_attr.url) if request else file_attr.url
        return None  # Retorna None si no existe el archivo
    
    def get_pdf_url(self, obj):
        return self.get_url(obj, 'file')


    
class MediaFileSerializer(serializers.ModelSerializer):
    """
        Clase que representa a un serealización del Media file y devuelve las urls correspondiente con sus escalas.
    """
    image_for_pc_url = serializers.SerializerMethodField()
    image_for_tablet_url = serializers.SerializerMethodField()
    image_for_mobile_url = serializers.SerializerMethodField()

    class Meta:
        model = MediaFile
        fields = ['file', 'title', 'uploaded_at', 'image_for_pc_url', 'image_for_tablet_url', 'image_for_mobile_url']

    def get_image_url(self, obj, attr_name):
        request = self.context.get('request')
        file_attr = getattr(obj, attr_name, None)
        
        if file_attr and hasattr(file_attr, 'url'):  # Verifica si tiene URL
            return request.build_absolute_uri(file_attr.url) if request else file_attr.url
        return None  # Retorna None si no existe el archivo

    def get_image_for_pc_url(self, obj):
        return self.get_image_url(obj, 'image_for_pc')

    def get_image_for_tablet_url(self, obj):
        return self.get_image_url(obj, 'image_for_tablet')

    def get_image_for_mobile_url(self, obj):
        return self.get_image_url(obj, 'image_for_mobile')