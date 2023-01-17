from rest_framework import serializers
from .models import Board, Keyword, Filter


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

class FilterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filter
        fields = ('id', 'authorr', 'title', 'keywordlist', 'emaillist')
