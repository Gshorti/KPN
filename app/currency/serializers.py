from rest_framework.serializers import ModelSerializer

from currency.models import Currency


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"