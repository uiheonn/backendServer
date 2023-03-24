from rest_framework import serializers
from .models import Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = (
            'id',
            'user',
            'folder_name',
            'sender',
            'keyword',
        )
    def validate_sender(self, value):
        if not value:
            # sender 값이 빈 리스트인 경우 "모든"으로 변경
            value = ["모든"]
        return value
    
    def validate_keyword(self, value):
        if not value:
            value = ["모든"]
        return value