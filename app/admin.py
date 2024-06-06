from django.contrib import admin

from app.models import Sample


# Register your models here.
@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    pass
