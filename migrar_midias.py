import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

import cloudinary.uploader

from Projeto_Bandas.models import Banda


demos = {
    "Metallica": "media/demos/For_Whom_The_Bell_Tolls_Remastered.mp3",
    "Megadeth": "media/demos/Tornado_Of_Souls_-_Megadeth_youtube.mp3",
    "Slipknot": "media/demos/Slipknot_-_The_Heretic_Anthem_Audio_-_Slipknot_youtube.mp3",
    "System Of Down": "media/demos/System_of_a_Down_-_Aerials_Remastered_2021.mp3",
}


for nome_banda, caminho in demos.items():
    try:
        print(f"Enviando demo: {nome_banda}")

        resultado = cloudinary.uploader.upload(
            caminho,
            resource_type="video"
        )

        url = resultado["secure_url"]

        banda = Banda.objects.get(nome=nome_banda)
        banda.demo_audio = url
        banda.save(update_fields=["demo_audio"])

        print(f"Demo salva: {nome_banda}")

    except Exception as erro:
        print(f"ERRO em {nome_banda}: {erro}")


print("Migração das demos finalizada!")