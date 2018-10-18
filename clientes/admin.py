from django.contrib import admin
from .models import Pessoas, Documento, Venda, Produto

# Register your models here.


admin.site.register(Pessoas)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)