
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from currency.models import Currency
from rest_framework.response import Response
from rest_framework import status
from currency.average import average_calculator
from currency.serializers import CurrencySerializer
from rest_framework.viewsets import ModelViewSet


class listValutaViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = "__all__"
    search_fields = ['name']



# Create your views here.
class Currencyview(APIView):
    def get(self, request, format=None):
        biba = Currency.objects.all()
        for boba in biba:
            name = boba.Name
            print(name)
            curr = Currency.objects.get(Name=name)
            sale_orders = curr.sale_orders
            buy_orders = curr.buy_orders
            print(sale_orders,buy_orders)
            sale_average, buy_average, average = average_calculator(sale_orders,buy_orders)
            curr.sale_price = sale_average
            curr.buy_price = buy_average
            curr.price = average
            curr.save()
        snippets = Currency.objects.all()
        serializer = CurrencySerializer(snippets, many=True)
        filter_backends = [DjangoFilterBackend, SearchFilter]
        filterset_fields = "__all__"
        search_fields = ['name']
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CurrencySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)