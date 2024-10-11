from typing import Any, Dict
from django import forms
from .models import Channel

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['title', 'image', 'language', 'subchannels', 'contents']
        required = ['title', 'image', 'language']

    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        cleaned_contents = cleaned_data.get('contents') and cleaned_data.get('contents').count()
        cleaned_subchannels = cleaned_data.get('subchannels')  and cleaned_data.get('subchannels').count()
        if cleaned_contents and cleaned_subchannels:
            raise forms.ValidationError('A channel should have only either subchannels or contents.')

        if not cleaned_subchannels and not cleaned_contents:
            raise forms.ValidationError("A channel should have subchanels or contents.")