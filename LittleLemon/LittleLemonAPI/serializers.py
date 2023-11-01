from rest_framework import serializers
from . models import MenuItem,Category
from decimal import Decimal





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','slug','title']


class MenuItemSerializer(serializers.ModelSerializer):
    price_after_taxes=serializers.SerializerMethodField(method_name='calculate_tax')
    #category=serializers.StringRelatedField()
    category=CategorySerializer() 
    class Meta:
        model=MenuItem
        fields=['id','title','price','inventory','price_after_taxes','category']

    def calculate_tax(self,product:MenuItem):
        return product.price*Decimal(1.1)