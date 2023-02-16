from rest_framework import serializers

from .models import Emaillist2User

class Emaillist2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emaillist2User
        fields = (
            'id',
            'email',
            'password',
            'g_key',
        )