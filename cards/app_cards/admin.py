from django.contrib import admin

from app_cards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['series', 'number', 'release_date', 'expiration_date', 'cvv', 'activity_flag']


admin.site.register(Card, CardAdmin)
