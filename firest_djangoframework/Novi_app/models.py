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







