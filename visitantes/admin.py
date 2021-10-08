from django.contrib import admin
from visitantes.models import Visitante  # type: ignore

admin.site.register(Visitante)
