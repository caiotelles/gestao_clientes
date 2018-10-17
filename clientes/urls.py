
from django.urls import path
from .views import pessoa_lista, pessoa_nova, pessoa_atualizar, pessoa_deletar



urlpatterns = [
    path('lista/', pessoa_lista, name="pessoa_lista"),
    path('novo/', pessoa_nova, name="pessoa_nova"),
    path('atualizar/<int:id>', pessoa_atualizar, name="pessoa_atualizar"),
    path('delete/<int:id>', pessoa_deletar, name="pessoa_deletar"),
]