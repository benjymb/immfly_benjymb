from .serializers import ChannelSerializer, ContentSerializer, SubChannelSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .exceptions import NotFound, InvalidParameters, PermissionDenied

class ChannelContentView(APIView):

    def get(self, request, channel_id, format=None):
        try:
            return Response(ChannelSerializer.get_contents_for_channel(channel_id))
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND) 
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 
        

class ContentView(APIView):

    def get(self, request, content_id, format=None):
        try:
            return Response(ContentSerializer.get_content(content_id))
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND) 
        except InvalidParameters as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST) 


class ChannelView(APIView):

    def get(self, request, format=None):
        try:
            return Response(ChannelSerializer.get_channels())
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)
        
class SubChannelView(APIView):

    def get(self, request, channel_id, format=None):
        try:
            return Response(SubChannelSerializer.get_channel_by_id(channel_id))
        except NotFound as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)