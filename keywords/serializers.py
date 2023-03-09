from rest_framework import serializers

from .models import KeywordUser

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordUser
        fields = (
            'id',
            'keyword',
        )