# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Nakit(models.Model):
    ogrlica_ime = models.CharField(max_length=10)
    ogrlica_opis = models.TextField(max_length=100)
    pristen_ime = models.CharField(max_length=10)
    prsten_opis = models.TextField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.ogrlica_ime, self.pristen_ime)


class Item(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Storage(models.Model):
    quantity = models.IntegerField(default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

    @property
    def item_description(self):
        return self.item.description


class Festival(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Festival {} is in the city {}".format(self.name, self.city)


class Stand(models.Model):
    NUMBER_STAND = (
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
    )

    number = models.PositiveSmallIntegerField(choices=NUMBER_STAND)
    stand = models.ForeignKey(Festival, on_delete=models.CASCADE)

    def __str__(self):
        return "{} use {} stand".format(self.stand.name, self.number)


class Music(models.Model):
    MUSIC_TYPE = (
        (1, "Rock"),
        (2, "Metal"),
        (3, "Rap"),
        (4, "Country")
    )

    mt = models.PositiveSmallIntegerField(choices=MUSIC_TYPE)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Your choice is {} music.".format(self.mt)


class Artist(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    artist_name = models.CharField(max_length=25)

    def __str__(self):
        return "Your artist name is {}.".format(self.artist_name)


class Album(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=40)
    num_song = models.IntegerField(default=0)

    def __str__(self):
        return "Your choice is {} music, your artist name is {} and name of yours album is {}!".format(self.music.mt, self.artist.artist_name, self.album_name)
