from django.contrib import admin

from .models import Cohort


class CohortAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(Cohort)
