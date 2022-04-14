from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(Patient)
