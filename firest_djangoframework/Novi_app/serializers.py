from rest_framework import serializers
from .models import Nakit, Item, Storage, Stand, Festival, Music, Artist, Album


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
            'stand_name',

        )

    festival_name = serializers.SerializerMethodField()

    def get_festival_name(self, stand):
        return stand.stand.name

    stand_name = serializers.SerializerMethodField()

    def get_stand_name(self, stand):
        return stand.get_number_display()


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = (
            'mt',
        )


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'first_name',
            'last_name',
            'artist_name',
        )


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'album_name',
            'num_song',
            'art_name',
            'music',
            'music_type',
            'artist',

            )

    art_name = serializers.SerializerMethodField()

    def get_art_name(self, artist):
        return artist.artist.artist_name

    music_type = serializers.SerializerMethodField()

    def get_music_type(self, music):
        return music.music.get_mt_display()
