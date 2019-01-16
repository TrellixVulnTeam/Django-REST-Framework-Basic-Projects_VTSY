from django.shortcuts import render
from rest_framework import viewsets
from Api.serializers import ProductSerializers
from Api.models import Product


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
