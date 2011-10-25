from beer.models import Brewery, Beer, Review, ReviewComment
from django.contrib import admin


class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brewery', 'abv', 'style', 'external_rating')
    search_fields = ['name']


class ReviewAdmin(admin.ModelAdmin):
    list_filter = ['date']
    date_hierarchy = 'date'


admin.site.register(Brewery)
admin.site.register(Beer, BeerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewComment)
