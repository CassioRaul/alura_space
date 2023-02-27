from django.urls import path, include
from galeria.views import galeria, imagem

urlpatterns = [
    path('', galeria, name="galeria"),
    path('imagem/', imagem, name="imagem"),
]

