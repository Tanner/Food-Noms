from reviews.models import * 
from django.contrib import admin

class RatingResponseInline(admin.TabularInline):
     model = RatingResponse
     extra = 0

class FreeResponseInline(admin.TabularInline):
     model = FreeResponse
     extra = 0

class ReviewAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'nom', 'user')
     inlines = [RatingResponseInline, FreeResponseInline];

class QuestionAdmin(admin.ModelAdmin):
     list_display = ('question', 'type') 
     list_filter = ('type',)

class RatingResponseAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'review', 'question', 'rate')
     list_filter = ('question',)

class FreeResponseAdmin(admin.ModelAdmin):
     list_display = ('__unicode__', 'review', 'question', 'freeResponse')
     list_filter = ('question',)

admin.site.register(Review, ReviewAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(RatingResponse, RatingResponseAdmin)
admin.site.register(FreeResponse, FreeResponseAdmin)
