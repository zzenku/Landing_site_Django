from django.contrib import admin

from price.models import PriceCard, PriceTable

admin.site.register(PriceCard)
admin.site.register(PriceTable)