# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class NoviAppConfig(AppConfig):
    name = 'firest_djangoframework.Novi_app'

    def ready(self):
        import firest_djangoframework.Novi_app.signals # noqa
