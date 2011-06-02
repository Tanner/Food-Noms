from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     (r'^$', 'noms.views.index'),
     (r'^noms/$', 'noms.views.search'),
     (r'^search/$', 'noms.views.search'),
     (r'^(?P<restaurant_id>\d+)/$', 'noms.views.restaurantDetail'),
     (r'^(?P<restaurant_id>\d+)/(?P<nom_id>\d+)$', 'noms.views.nomDetail')
    # Examples:
    # url(r'^$', 'food_noms.views.home', name='home'),
    # url(r'^food_noms/', include('food_noms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
