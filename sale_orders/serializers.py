from rest_framework import serializers
from .models import SaleOrder, SaleOrderItem


class SaleOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderItem
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        order = validated_data.get('order')
        item = validated_data.get('item')
        qty = validated_data.get('qty') 
        ...
        return super().create(validated_data)


class SaleOrderSerializer(serializers.ModelSerializer):
    sale_items = SaleOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = SaleOrder
        fields = '__all__'
