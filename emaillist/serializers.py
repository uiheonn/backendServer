from rest_framework import serializers

from .models import EmaillistUser

class EmaillistSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmaillistUser
        fields = (
            'id',
            'g_email',
            'g_password',
            'g_key',
            'n_email',
            'n_password',
        )