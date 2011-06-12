from django.conf.urls.defaults import *

urlpatterns = patterns('',
          url(r'^delete/(?P<rating_id>\d+)/$', 'ratings.views.delete', name='rating_delete'),
          url(r'^add/(?P<nom_id>\d+)/$', 'ratings.views.add', name='rating_add'),
          url(r'^(?P<rating_id>\d+)/$', 'ratings.views.detail', name='rating_detail'),
          )
