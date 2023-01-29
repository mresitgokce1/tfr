from django.db import models
from utils.models import BaseEntity
import uuid


class Location(BaseEntity):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fsq_id = models.CharField(verbose_name="FSQ ID", max_length=255, blank=True, null=True, unique=True)
    latitude = models.FloatField(verbose_name="Enlem", blank=False, null=False)
    longitude = models.FloatField(verbose_name="Boylam", blank=False, null=False)
    address = models.TextField(verbose_name="Adres", blank=True, null=True)
    country = models.CharField(verbose_name="Ülke", max_length=255, blank=True, null=True)
    region = models.CharField(verbose_name="Bölge", max_length=255, blank=True, null=True)
    name = models.CharField(verbose_name="İsim", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
