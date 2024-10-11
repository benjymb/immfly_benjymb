from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .exceptions import NotFound

import uuid

from .constants import LANGUAGES, METADATA_TYPES

class MetadataType(models.Model):
    metadata_type = models.TextField(max_length=250, unique=True)


class Content(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    file = models.FileField(upload_to="files/contents")
    rating = models.PositiveIntegerField()


class ContentMetadata(models.Model):
    metadata = models.TextField()
    metadata_type = models.ForeignKey(MetadataType, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['metadata_type', 'content']


class Channel(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    title = models.CharField(max_length=1024)
    image = models.ImageField(upload_to="files/channels")
    language = models.CharField(max_length=3, choices=LANGUAGES.choices())
    subchannels = models.ManyToManyField("self", blank=True)
    contents = models.ManyToManyField(Content, blank=True)

    @classmethod
    def get_channels(cls):
        return cls.objects.filter(subchannels__isnull=False).distinct()
    
    @classmethod
    def get_channel_by_id(cls, channel_id):
        try:
            return cls.objects.get(pk=channel_id)
        except cls.DoesNotExist:
            raise NotFound("The channel does not exists.")
