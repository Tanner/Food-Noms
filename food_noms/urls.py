from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from food_noms.userprofiles.forms import ProfileForm
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'noms.views.index', name='home'),
     url(r'^search/$', 'noms.views.search', name='search'),
     url(r'^(?P<restaurant_id>\d+)/$', 'noms.views.restaurantDetail', name='restaurant_detail'),
     url(r'^(?P<restaurant_id>\d+)/(?P<nom_id>\d+)/$', 'noms.views.nomDetail', name='nom_detail'),

     (r'^review/', include('food_noms.reviews.urls')),

     (r'^accounts/', include('registration.urls')),

     ('^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),
     (r'^profiles/', include('profiles.urls')),
     
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
