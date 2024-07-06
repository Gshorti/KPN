from rest_framework import serializers

from KPN.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Telegram_hash', 'KPСS']
