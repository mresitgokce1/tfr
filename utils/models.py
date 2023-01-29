from django.db import models


class BaseEntity(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name="Aktif Mi?", default=True,
                                    blank=False, null=False)
    is_deleted = models.BooleanField(verbose_name="Silindi Mi?", default=False,
                                     blank=False, null=False)

    class Meta:
        abstract = True
