from rest_framework import serializers
from core.models import TODO


class TODOserializer(serializers.ModelSerializer):
    class Meta:
        model=TODO
        fields = ['id', 'title', 'description', 'completed', 'created_at']