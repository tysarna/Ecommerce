from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What Tag is applied to what item/object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # What item/object is tagged
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()