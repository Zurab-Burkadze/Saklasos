from .models import PurchaseOrder, PurchaseOrderItem
from rest_framework import serializers


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

        def create(self, validated_data):
            print(validated_data)
            order = validated_data.get('order')
            item = validated_data.get('item')
            qty = validated_data.get('qty') 
            ...
            return super().create(validated_data)



class PurchaseOrderSerializer(serializers.ModelSerializer):
    order_items = PurchaseOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'





