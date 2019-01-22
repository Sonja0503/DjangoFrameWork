from django.db.models.signals import post_save
from .models import Item, Storage, Festival, Stand
from django.dispatch import receiver


@receiver(post_save, sender=Item)
def create_item_storage(sender, instance, created, **kwargs):
    print(created)
    print(instance)
    if created:
        storage = Storage()
        storage.item = instance
        storage.quantity = 5
        storage.save()


@receiver(post_save, sender=Festival)
def create_fest_stand(sender, instance, created, **kwargs):
    if created:
        stand = Stand()
        stand.stand = instance
        stand.number = 5
        stand.save()
