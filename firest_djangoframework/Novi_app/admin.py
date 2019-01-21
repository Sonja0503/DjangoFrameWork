# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Nakit
from .models import Storage
from .models import Item


class NakitAdmin(admin.ModelAdmin):
    list_display = ('ogrlica_ime', 'ogrlica_opis', 'pristen_ime', 'prsten_opis')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


class StorageAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'item', 'price')

    def price(self, storage):
        return storage.item.price


admin.site.register(Nakit, NakitAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Item, ItemAdmin)
