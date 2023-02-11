from rest_framework import serializers
<<<<<<< HEAD
from .models import Keyword, Board
=======
from .models import Board, Keyword, Filter

>>>>>>> 0327693067534ab5ff41e7507bb778fe7c46cc9f

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

<<<<<<< HEAD
'''
class FilteringSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filtering
        fields = ('id', 'filter_author', 'title', 'keywordlist', 'emaillist')
'''
=======
class FilterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filter
        fields = ('id', 'authorr', 'title', 'keywordlist', 'emaillist')
>>>>>>> 0327693067534ab5ff41e7507bb778fe7c46cc9f
