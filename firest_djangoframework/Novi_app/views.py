# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Nakit, Storage, Item
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .serializers import NakitSerializer, StorageSerializer, ItemSerializer, StorageDetailSerializer


class NakitMixin(object):
    def get_object(self):
        id = self.kwargs['id']
        nakit = Nakit.objects.get(id=id)
        print(self.kwargs)
        return nakit


class StorageMixin(object):

    def get_object(self):

        id = self.kwargs['item_id']
        storage = Storage.objects.get(item__id=id)
        print(Storage.quantity)
        print(storage.quantity)
        return storage


class ItemMixin(object):
    def get_object(self):
        id = self.kwargs['id']
        storage = Item.objects.get(id=id)
        return storage


class NakitListView(ListAPIView):
    serializer_class = NakitSerializer

    # vraca listu
    def get_queryset(self):
        nakit = Nakit.objects.filter(ogrlica_ime='Mozak')
        return nakit


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
        serializer.save()

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
        serializer.save()
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







