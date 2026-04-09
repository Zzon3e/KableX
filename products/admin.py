from django.contrib import admin
from .models import Medlem, Aktivitet, Pamelding, Betaling

@admin.register(Medlem)
class MedlemAdmin(admin.ModelAdmin):
    list_display = ('navn', 'epost', 'telefon', 'medlemsdato', 'aktiv')
    list_filter = ('aktiv', 'medlemsdato')
    search_fields = ('navn', 'epost')

@admin.register(Aktivitet)
class AktivitetAdmin(admin.ModelAdmin):
    list_display = ('navn', 'dato', 'sted')
    list_filter = ('dato',)
    search_fields = ('navn', 'beskrivelse')

@admin.register(Pamelding)
class PameldingAdmin(admin.ModelAdmin):
    list_display = ('medlem', 'aktivitet', 'dato_pameldt')
    list_filter = ('dato_pameldt', 'aktivitet')
    search_fields = ('medlem__navn', 'aktivitet__navn')

@admin.register(Betaling)
class BetalingAdmin(admin.ModelAdmin):
    list_display = ('medlem', 'belop', 'betalingsdato', 'status')
    list_filter = ('status', 'betalingsdato')
    search_fields = ('medlem__navn',)