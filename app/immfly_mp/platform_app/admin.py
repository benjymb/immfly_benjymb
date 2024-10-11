from django.contrib import admin
from .models import Content, Channel, ContentMetadata, MetadataType
from .forms import ChannelForm

class ContentMetadataAdmin(admin.TabularInline):
    model = ContentMetadata

class ContentAdmin(admin.ModelAdmin):
    model = Content
    inlines = [ContentMetadataAdmin]

class ChannelAdmin(admin.ModelAdmin):
    model = Channel
    form = ChannelForm

admin.site.register(Channel, ChannelAdmin)
admin.site.register(MetadataType)
admin.site.register(Content, ContentAdmin)
