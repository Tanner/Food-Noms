from noms.models import Restaurant, Nom
from django.contrib import admin

class NomInline(admin.TabularInline):
     model = Nom
     extra = 1

class RestaurantAdmin(admin.ModelAdmin):
     inlines = [NomInline]

class NomAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'restaurant')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Nom, NomAdmin)
