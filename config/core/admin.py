from django.contrib import admin
from django import forms

from .models import URL, Profile


class URLAdminForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = '__all__'


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    form = URLAdminForm
    list_display = ('id', 'full_url', 'short_url', 'clicks', 'created_at')
