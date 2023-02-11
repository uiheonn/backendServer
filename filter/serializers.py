from rest_framework import serializers
from .models import Filter

class FilterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filter
        fields = ('id', 'filter_author', 'title', 'keywordlist', 'emaillist')