from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

model_list = [Predavac, Tecaj, Prebivaliste, Polaznik, Ocjena, TjedanRadnoVrijeme, Raspored]
admin.site.register(model_list)