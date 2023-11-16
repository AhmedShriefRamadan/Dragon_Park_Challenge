from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    kind = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(ContentType,
                                blank=True,
                                null=True,
                                related_name='target_obj',
                                on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,blank=True)
    target = GenericForeignKey('target_ct','target_id')

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['target_ct','target_id']),
        ]
        ordering = ['-created']