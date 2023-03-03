from rest_framework import serializers
from .models import Folder2

class Folder2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Folder2
        fields = (
            'id',
            'user',
            'folder_name',
            'sender',
            'keyword',
            'email_domain',
        )