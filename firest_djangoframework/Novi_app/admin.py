# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Nakit, Storage, Stand, Item, Festival, Music, Artist, Album


class NakitAdmin(admin.ModelAdmin):
    list_display = ('ogrlica_ime', 'ogrlica_opis', 'pristen_ime', 'prsten_opis')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


class StorageAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'item', 'price')

    def price(self, storage):
        return storage.item.price


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'description')


class StandAdmin(admin.ModelAdmin):
    list_display = ('number', 'id', 'name')

    def name(self, stand):
        return stand.stand.name


class MusicAdmin(admin.ModelAdmin):
    list_display = ('mt',)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'artist_name')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'num_song', 'type', 'name')

    def type(self, mus):
        return mus.music.mt

    def name(self, name):
        return name.artist.artist_name


admin.site.register(Nakit, NakitAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Stand, StandAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
