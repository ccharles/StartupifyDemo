from beer.models import Brewery, Beer, Review
from django.contrib import admin


class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brewery', 'abv', 'style')


admin.site.register(Brewery)
admin.site.register(Beer, BeerAdmin)
admin.site.register(Review)
