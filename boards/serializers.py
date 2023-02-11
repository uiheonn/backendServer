from rest_framework import serializers
from .models import Keyword, Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = (
                #'author',
                'id', 
                'keyword', 
                'mail',
                'created_at', 
                'modified_at'
                )


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = (
            #'key',
            'id',
            'keyword',
            'mail'
        )