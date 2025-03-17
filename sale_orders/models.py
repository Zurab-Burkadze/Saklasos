from django.db import models
from core.models import BaseModel
from items.models import Item

def generate_order_name():
    last_order = SaleOrder.objects.order_by('-id').first()
    if last_order:
        return f'S0000{last_order.id+1}'
    return 'S00001'

class SaleOrder(BaseModel):
    name = models.CharField(max_length=250, default=generate_order_name, editable=False, unique=True)
    completed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name

class SaleOrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="sale_items")
    qty = models.PositiveIntegerField(default=0)
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, related_name='sale_items')

