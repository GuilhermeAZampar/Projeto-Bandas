from django.contrib import admin
from django.urls import path, include
from .views import home,detalhes,nova_banda,editar_banda,excluir_banda,novo_integrante,editar_integrante,excluir_integrante,cadastrar_disco,editar_disco,excluir_disco
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",home,name="home"),
    path("detalhes/<int:id>/",detalhes,name="detalhes"),
    path("nova_banda/",nova_banda,name="nova_banda"),
    path("editar_banda/<int:id>/",editar_banda,name="editar_banda"),
    path("excluir_banda/<int:id>/",excluir_banda,name="excluir_banda"),
    path("novo_integrante/<int:id>/",novo_integrante,name="novo_integrante"),
    path("editar_integrante/<int:id>/",editar_integrante,name="editar_integrante"),
    path("excluir_integrante/<int:id>/",excluir_integrante,name="excluir_integrante"),
    path("cadastrar_disco/<int:id>/",cadastrar_disco,name="cadastrar_disco"),
    path("editar_disco/<int:id>/",editar_disco,name="editar_disco"),
    path("excluir_disco/<int:id>/",excluir_disco,name="excluir_disco"),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)