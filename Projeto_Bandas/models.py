from django.db import models
from django.contrib.auth.models import User


class Banda(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bandas')
    nome=models.CharField(max_length=100)
    estilo=models.CharField(max_length=100)
    descricao_banda=models.TextField(max_length=500)
    demo_audio=models.URLField(blank=True)

    spotify = models.URLField(blank=True)
    apple_music = models.URLField(blank=True)
    youtube_music = models.URLField(blank=True)
    amazon_music = models.URLField(blank=True)
    deezer = models.URLField(blank=True)

    instagram = models.URLField(blank=True)
    x = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    youtube=models.URLField(blank=True)

    foto=models.ImageField(upload_to='banda/',blank=True)

    def __str__(self):
        return self.nome




class Integrantes(models.Model):
    banda=models.ForeignKey(Banda,on_delete=models.CASCADE,related_name='integrantes')
    nome=models.CharField(max_length=200)
    instrumento=models.CharField(max_length=100)

    def __str__(self):
        return self.nome




class Discos(models.Model):
    banda=models.ForeignKey(Banda,on_delete=models.CASCADE,related_name='discos')
    nome=models.CharField(max_length=200)
    descricao_disco=models.TextField(max_length=500)
    ano=models.PositiveIntegerField()
    capa=models.ImageField(upload_to='discos/',blank=True)

    def __str__(self):
        return self.nome


