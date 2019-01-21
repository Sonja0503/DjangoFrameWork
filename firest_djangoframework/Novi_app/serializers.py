from rest_framework import serializers
from .models import Nakit
from .models import Item
from .models import Storage


class NakitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nakit
        fields = (
            'ogrlica_ime',
            'ogrlica_opis',
            'prsten_opis'
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'name',
            'price',
            'description',
            'id'
        )


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            'item',
            'quantity',
            'item_price',
            'i_price'
        )
    # from Item
    item = ItemSerializer()

    item_price = serializers.CharField(read_only=True, source="item.price")
    # from Item
    i_price = serializers.SerializerMethodField()

    def get_i_price(self, storage):
        return storage.item.price


class StorageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            'quantity',
            'item'
        )
