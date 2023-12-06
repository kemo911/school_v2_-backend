from rest_framework import serializers
from ..models import CourseCatalog


class CourseCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCatalog
        fields = '__all__'
