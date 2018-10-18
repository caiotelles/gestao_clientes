from django.contrib import admin
from .models import Pessoas, Venda, Produto

# Register your models here.


admin.site.register(Pessoas)
admin.site.register(Venda)
admin.site.register(Produto)