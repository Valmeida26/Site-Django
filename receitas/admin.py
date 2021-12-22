from django.contrib import admin
#Esta importando em models a class Receita
from .models import Receita

admin.site.register(Receita)