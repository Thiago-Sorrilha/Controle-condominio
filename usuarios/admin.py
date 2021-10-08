from django.contrib import admin
from usuarios.models import Usuario  # type: ignore

admin.site.register(Usuario)
