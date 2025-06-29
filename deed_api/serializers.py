from rest_framework import serializers
from .models import FieldPosition

class FieldPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldPosition
        fields = ['field_name', 'x', 'y', 'is_global']