from typing import Any, Dict, List
from rest_framework import serializers
from .models import Channel, Content, ContentMetadata
from .exceptions import NotFound

class ContentMetadataSerializer(serializers.ModelSerializer):

    metadata_name = serializers.SerializerMethodField()

    class Meta:
        model = ContentMetadata
        fields = ['metadata_name', 'metadata']

    def get_metadata_name(self, obj):
        return obj.metadata_type.metadata_type

class ContentSerializer(serializers.ModelSerializer):

    metadata = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ['id', 'file', 'rating', 'metadata']

    def get_metadata(self, obj):
        metadata = ContentMetadata.objects.filter(content=obj.pk).all()
        return ContentMetadataSerializer(metadata, many=True).data

    @staticmethod
    def get_content(content_id):
        try:
            return ContentSerializer(Content.objects.get(pk=content_id)).data
        except Content.DoesNotExist:
            raise NotFound("This content doesnt exist.")
        


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'image', 'language', 'subchannels']

    @staticmethod
    def get_channels():
        return ChannelSerializer(Channel.get_channels(), many=True).data
    
    @staticmethod
    def get_contents_for_channel(channel_id):
        try:
            channel = Channel.objects.get(pk=channel_id)
            if channel.contents.count():
                return ContentSerializer(channel.contents.all(), many=True).data
            else:
                raise NotFound("This channel doesnt have contents.")
        except Channel.DoesNotExist:
            raise NotFound("This channel doesnt exist.")
    

class SubChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ['id', 'title', 'image', 'language', 'contents']

    @staticmethod
    def get_channel_by_id(channel_id):
        try:
            return SubChannelSerializer(Channel.get_channel_by_id(channel_id)).data
        except Channel.DoesNotExist:
            raise NotFound("This channel doesnt exist.")
    

