from ratings.models import Rating, Question, Response
from django.contrib import admin

class ResponseInline(admin.TabularInline):
     model = Response
     extra = 1

class RatingAdmin(admin.ModelAdmin):
     inlines = [ResponseInline]

admin.site.register(Rating, RatingAdmin)
admin.site.register(Question)
admin.site.register(Response)
