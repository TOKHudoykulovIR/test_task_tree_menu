from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=120)
    url = models.CharField(max_length=255, blank=True, null=True)


class MenuItem(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children", blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
