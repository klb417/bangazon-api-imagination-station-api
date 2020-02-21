"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for park areas

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = Order
        # creates a clickable url for the API
        url = serializers.HyperlinkedIdentityField(
            view_name="order",
            lookup_field='id'
        )
        fields = ('id', 'created_at', 'customer', 'payment_type')

        