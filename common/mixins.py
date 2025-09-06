# reusable logic like soft delete and status tracking

from django.db import models

class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
