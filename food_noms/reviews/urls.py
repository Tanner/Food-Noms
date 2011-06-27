from django.conf.urls.defaults import *

urlpatterns = patterns('',
          url(r'^delete/(?P<review_id>\d+)/$', 'reviews.views.delete', name='review_delete'),
          url(r'^add/(?P<nom_id>\d+)/$', 'reviews.views.add', name='review_add'),
          url(r'^(?P<review_id>\d+)/$', 'reviews.views.detail', name='review_detail'),
          )
