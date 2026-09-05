from django import forms
from django.forms import ModelForm
from .models import Banda,Integrantes,Discos

class BandaForm(ModelForm):
    demo_audio_url=forms.URLField(required=False,widget=forms.HiddenInput())
    class Meta:
        model= Banda
        fields=[
            'nome',
            'estilo',
            'descricao_banda',

            'spotify',
            'apple_music',
            'youtube_music',
            'amazon_music',
            'deezer',

            'instagram',
            'x',
            'tiktok',
            'youtube',

            'foto',
        ]


class IntegranteForm(ModelForm):
    class Meta:
        model = Integrantes
        fields=[
            'nome',
            'instrumento'
        ]


class DiscoForm(ModelForm):
    class Meta:
        model= Discos
        fields=[
            'nome',
            'descricao_disco',
            'ano',
            'capa'
        ]