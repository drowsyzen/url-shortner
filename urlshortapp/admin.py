from django.contrib import admin
from urlshortapp.models import URLModel
# Register your models here.


@admin.register(URLModel)
class URLModelAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["original_url", "status", "created_at", "redirect_url"]
