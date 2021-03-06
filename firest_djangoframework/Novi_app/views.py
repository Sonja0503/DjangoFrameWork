# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Nakit, Storage, Item, Festival, Stand, Music, Artist, Album
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .serializers import NakitSerializer, StorageSerializer, ItemSerializer, StorageDetailSerializer, FestivalSerializer, StandSerializer, MusicSerializer, ArtistSerializer, AlbumSerializer


class NakitMixin(object):
    def get_object(self):
        id = self.kwargs['id']
        nakit = Nakit.objects.get(id=id)
        print(self.kwargs)
        return nakit


class StorageMixin(object):

    def get_object(self):

        id = self.kwargs['id']
        storage = Storage.objects.get(id=id)
        print(storage.item_description)
        return storage


class ItemMixin(object):
    def get_object(self):
        id = self.kwargs['id']
        storage = Item.objects.get(id=id)
        return storage


class FestivalMixin(object):
    def get_object(self):
        id = self.kwargs['id']
        fest = Festival.objects.get(id=id)
        return fest


class StandMixin(object):
    def get_object(self):
        id = self.kwargs['stand_id']
        stand = Stand.objects.get(stand__id=id)
        return stand


class NakitListView(ListAPIView):
    serializer_class = NakitSerializer

    # vraca listu
    def get_queryset(self):
        qs = Nakit.objects.all()
        prsten = self.request.query_params.get('prsten')
        ogrlica = self.request.query_params.get('ogrlica')
        if prsten:
            qs = qs.filter(pristen_ime__icontains=prsten)
        if ogrlica:
            qs = qs.filter(ogrlica_ime__icontains=ogrlica)
        return qs


class NakitRetrieveView(RetrieveAPIView):
    serializer_class = NakitSerializer
    queryset = Nakit.objects.all()
    lookup_url_kwarg = 'nakit_id'


class NakitCreateView(CreateAPIView):
    serializer_class = NakitSerializer
    queryset = Nakit.objects.all()

    def create(self, request, *args, **kwargs):
        nakit = request.data
        print(request.data)
        serializer = self.get_serializer(data=nakit)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
        )


class NakitUpdateView(NakitMixin, UpdateAPIView):
    serializer_class = NakitSerializer
    queryset = Nakit.objects.all()

    def update(self, request, *args, **kwargs):
        nakit = self.get_object()
        serializer = self.get_serializer(nakit, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(kwargs)
        return Response(
            serializer.data, status=status.HTTP_200_OK,
        )


class NakitDestroyView(NakitMixin, DestroyAPIView):

    serializer_class = NakitSerializer
    queryset = Nakit.objects.all()
    lookup_url_kwarg = 'id'


class StorageListView(ListAPIView):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()


class StorageRetrieveView(StorageMixin, RetrieveAPIView):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()


class ItemCreateView(CreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def create(self, request, *args, **kwargs):
        item = request.data
        serializer = self.get_serializer(data=item)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=request.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
                        )


class ItemUpdateView(UpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_url_kwarg = 'id'

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        # jednako je ItemSerializer-u
        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=item, validated_data=request.data)
        return Response(
            serializer.data, status=status.HTTP_200_OK,
                        )


class StorageCreateView(CreateAPIView):
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()

    def create(self, request, *args, **kwargs):
        storage = request.data
        item_id = request.data.get('item')
        try:
            item = Item.objects.get(id=item_id)
            print(request.data)
        except Item.DoesNotExist:
            item = Item()
            item.name = "Ines"
            item.price = 34.24
            item.description = "ijijiji"
            item.save()

        # item = Item.objects.create(name='Sonja', price=12.45, description='uuuuuuuu')

        serializer = self.get_serializer(data=storage)
        serializer.is_valid(raise_exception=True)
        serializer.save(item=item)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
        )


class StoregeUpdateView(StorageMixin, UpdateAPIView):
    serializer_class = StorageDetailSerializer
    queryset = Storage.objects.all()

    def update(self, request, *args, **kwargs):
        storage = self.get_object()
        serializer = self.get_serializer(storage, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(

            serializer.data, status=status.HTTP_200_OK,
        )


class FestivalListView(ListAPIView):
    serializer_class = FestivalSerializer

    def get_queryset(self):
        fest = Festival.objects.filter(name="ReArt")
        return fest


class FestivalRetrieveView(FestivalMixin, RetrieveAPIView):
    serializer_class = FestivalSerializer
    queryset = Festival.objects.all()


class FestivalUpdateView(FestivalMixin, UpdateAPIView):
    serializer_class = FestivalSerializer
    queryset = Festival.objects.all()

    def update(self, request, *args, **kwargs):
        fest = self.get_object()
        serializer = self.get_serializer(fest, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )


class FestivalCreateView(CreateAPIView):
    serializer_class = FestivalSerializer
    queryset = Festival.objects.all()

    def create(self, request, *args, **kwargs):
        fest = request.data
        serializer = self.get_serializer(data=fest)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class FestivalDestroyView(FestivalMixin, DestroyAPIView):
    serializer_class = FestivalSerializer
    queryset = Festival.objects.all()
    lookup_url_kwarg = 'id'


class StandRetrieveView(StandMixin, RetrieveAPIView):
    serializer_class = StandSerializer
    queryset = Stand.objects.all()


class StandUpdateView(StandMixin, UpdateAPIView):
    serializer_class = StandSerializer
    queryset = Stand.objects.all()

    def update(self, request, *args, **kwargs):
        stand = self.get_object()
        serializer = self.get_serializer(stand, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )


class StandListView(ListAPIView):
    serializer_class = StandSerializer

    def get_queryset(self):
        qs = Stand.objects.all()
        # dohvacanje iz Standa po query parametrima ,po kljucu
        city = self.request.query_params.get('city')
        number = self.request.query_params.get('number')
        name = self.request.query_params.get('name')
        # ako city postoji, filtriraj po njemu
        if city:
            qs = qs.filter(stand__city__icontains=city)
        if number:
            qs = qs.filter(number=number)
        if name:
            qs = qs.filter(stand__name__icontains=name)
        return qs


class StandCreateView(CreateAPIView):
    serializer_class = StandSerializer
    queryset = Stand.objects.all()

    def create(self, request, *args, **kwargs):
        stand = request.data
        fest_id = request.data.get('stand')
        try:
            sta = Festival.objects.get(id=fest_id)

        except Stand.DoesNotExist:
            sta = Festival()
            sta.name = "ArtLand"
            sta.city = "Novi-Sad"
            sta.description = "Veliki art fest"
            sta.save()

        serializer = self.get_serializer(data=stand)
        serializer.is_valid(raise_exception=True)
        serializer.save(stand=sta)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class StandDestroyView(StandMixin, DestroyAPIView):
    serializer_class = StandSerializer
    queryset = Stand.objects.all()
    lookup_url_kwarg = 'stand_id'


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get_object(self):
        id = self.kwargs['id']
        storage = Item.objects.get(id=id)
        return storage

    def retrieve(self, request, *args, **kwargs):
        # to je metoda get_object
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        self.perform_destroy(item)
        return Response(
            status=status.HTTP_200_OK
        )


class MusicList(ListAPIView):
    serializer_class = MusicSerializer

    def get_queryset(self):
        qs = Music.objects.all()
        music_type = self.request.query_params.get('type')
        if music_type:
            qs = qs.filter(mt=music_type)
        return qs


class ArtistList(ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        qs = Artist.objects.all()
        an = self.request.query_params.get('artist')
        if an:
            qs = qs.filter(artist_name__icontains=an)
        return qs


class AlbumList(ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        qs = Album.objects.all()
        album = self.request.query_params.get('album')
        if album:
            qs = qs.filter(album_name=album)
        return qs


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()

    def get_object(self):
        id = self.kwargs['id']
        music = Music.objects.get(id=id)
        return music

    def retrieve(self, request, *args, **kwargs):
        music = self.get_object()
        serializer = self.get_serializer(music)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        music = self.get_object()
        serializer = self.get_serializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        music = self.get_object()
        self.perform_destroy(music)
        return Response(
            status=status.HTTP_200_OK
        )


class MusicCreateView(CreateAPIView):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()

    def create(self, request, *args, **kwargs):
        music = request.data
        serializer = self.get_serializer(data=music)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def get_object(self):
        id = self.kwargs['id']
        artist = Artist.objects.get(id=id)
        return artist

    def retrieve(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = self.get_serializer(artist)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = self.get_serializer(artist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        artist = self.get_object()
        self.perform_destroy(artist)
        return Response(
            status=status.HTTP_200_OK
        )


class ArtistCreateView(CreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def create(self, request, *args, **kwargs):
        artist = request.data
        serializer = self.get_serializer(data=artist)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def get_object(self):
        id = self.kwargs['id']
        album = Album.objects.get(id=id)
        return album

    def retrieve(self, request, *args, **kwargs):
        album = self.get_object()
        serializer = self.get_serializer(album)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        album = self.get_object()
        serializer = self.get_serializer(album, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        album = self.get_object()
        self.perform_destroy(album)
        return Response(
            status=status.HTTP_200_OK
        )


class AlbumCreateView(CreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def create(self, request, *args, **kwargs):
        album = request.data
        artist_id = request.data.get('artist')
        music_id = request.data.get('music')
        try:
            art = Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            art = Artist()
            art.first_name = "Sofija"
            art.last_name = "Strava"
            art.artist_name = "Sofoklo"
            art.save()

        try:
            mus = Music.objects.get(id=music_id)
        except Music.DoesNotExist:
            mus = Music()
            mus.mt = 1
            mus.save()

        serializer = self.get_serializer(data=album)
        serializer.is_valid(raise_exception=True)
        serializer.save(artist=art, music=mus)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )
