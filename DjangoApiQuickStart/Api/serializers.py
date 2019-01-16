from rest_framework import serializers
from Api.models import Product

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"