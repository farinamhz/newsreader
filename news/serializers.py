from rest_framework import serializers
from .models import Item, Channel


class ItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ChannelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"
