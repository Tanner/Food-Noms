from noms.models import Restaurant, Nom
from django.contrib import admin

class NomInline(admin.TabularInline):
     model = Nom
     extra = 1

class RestaurantAdmin(admin.ModelAdmin):
     inlines = [NomInline]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Nom)
