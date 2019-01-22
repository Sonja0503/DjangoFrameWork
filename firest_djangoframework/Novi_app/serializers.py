from rest_framework import serializers
from .models import Nakit
from .models import Item
from .models import Storage
from .models import Festival
from .models import Stand


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

    def create(self, validated_data):
        name = validated_data.get('name')
        price = validated_data.get('price')
        description = validated_data.get('description')
        item = Item()
        item.name = name
        item.price = price
        item.description = description
        item.save()
        return item

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = (
            'item',
            'quantity',
            'item_price',
            'i_price',
            'id',
            'item_description'
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


class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = (
            'name',
            'city',
            'description',
        )


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = (
            'number',
            'stand',
            'festival_name',

        )

    festival_name = serializers.SerializerMethodField()

    def get_festival_name(self, stand):
        return stand.stand.name
