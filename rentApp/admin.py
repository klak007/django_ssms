from django.contrib import admin
from .models import Rower, Klient, Wypozyczenia, Oplata, Salon, Pracownicy

admin.site.register(Klient)
#admin.site.register(Rower)
admin.site.register(Wypozyczenia)
admin.site.register(Oplata)
admin.site.register(Salon)
admin.site.register(Pracownicy)

@admin.register(Rower)
class RowerAdmin(admin.ModelAdmin):
    list_display = ('id_roweru', 'marka', 'model', 'id_salonu', 'koszt', 'wysokosc', 'kolor', 'przeznaczenie_plciowe', 'material_ramy', 'rodzaj_roweru')
    list_filter = ( 'marka', 'id_salonu', 'kolor', 'przeznaczenie_plciowe', 'material_ramy', 'rodzaj_roweru')
    search_fields = ( 'marka', 'kolor', 'przeznaczenie_plciowe', 'material_ramy', 'rodzaj_roweru')

    # ...

# Register your models here.
