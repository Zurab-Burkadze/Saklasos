from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import SaleOrderSerializer, SaleOrderItemSerializer
from .models import SaleOrder, SaleOrderItem
from rest_framework.decorators import action
from  rest_framework.response import Response



class SaleOrderViewSet(ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    @action(detail=True, methods=['post'])
    def validate(self, request, pk):
        sale_order = SaleOrder.objects.get(pk=pk)
        if sale_order.completed:
            return Response({'Sale Order is already validated.'})

        for sale_item in sale_order.sale_items.all():
            item = sale_item.item

            if item.stock_qty < sale_item.qty:
                return Response({f'{item} is not left in stock'})

            item.stock_qty -= sale_item.qty
            item.save()
        sale_order.completed = True
        sale_order.save()
        return  Response({'Order has been completed'})


class SaleOrderItemViewSet(ModelViewSet):

    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer
