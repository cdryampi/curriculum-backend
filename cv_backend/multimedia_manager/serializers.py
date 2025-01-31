from rest_framework import serializers
from .models import MediaFile, DocumentFile
from cv_backend.settings import URL_SERVER

class DocumentFileSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = DocumentFile
        fields = ['title', 'file', 'pdf_url']

    def get_pdf_url(self, obj):
        return URL_SERVER + obj.file.url if obj.file else None


    
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

    def get_image_for_pc_url(self, obj):
        request = self.context.get('request') # recupera el request
        return request.build_absolute_uri(obj.image_for_pc.url) if obj.image_for_pc else None

    def get_image_for_tablet_url(self, obj):
        request = self.context.get('request') # recupera el request
        return request.build_absolute_uri(obj.image_for_tablet.url) if obj.image_for_tablet else None

    def get_image_for_mobile_url(self, obj):
        request = self.context.get('request') # recupera el request
        return request.build_absolute_uri(obj.image_for_mobile.url) if obj.image_for_mobile else None
