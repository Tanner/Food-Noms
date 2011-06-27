from ratings.models import * 
from django.contrib import admin

class RatingResponseInline(admin.TabularInline):
     model = RatingResponse
     extra = 0

class FreeResponseInline(admin.TabularInline):
     model = FreeResponse
     extra = 0

class RatingAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'nom', 'user')
     inlines = [RatingResponseInline, FreeResponseInline];

class QuestionAdmin(admin.ModelAdmin):
     list_display = ('question', 'type') 
     list_filter = ('type',)

class RatingResponseAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'rating', 'question', 'rate')
     list_filter = ('question',)

class FreeResponseAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'rating', 'question', 'freeResponse')
     list_filter = ('question',)

admin.site.register(Rating, RatingAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(RatingResponse, RatingResponseAdmin)
admin.site.register(FreeResponse, FreeResponseAdmin)
