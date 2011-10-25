from django.conf.urls.defaults import *

urlpatterns = patterns('beer.views',
    # Examples:
    # url(r'^$', 'startupifydemo.views.home', name='home'),
    # url(r'^startupifydemo/', include('startupifydemo.foo.urls')),
    url(r'^$', 'index'),
    url(r'^brewery/(?P<brewery_id>\d+)/$', 'brewery'),
    url(r'^beer/(?P<beer_id>\d+)/$', 'beer'),
    url(r'^review/(?P<review_id>\d+)/$', 'review'),
    url(r'^review/(?P<review_id>\d+)/comment/$', 'review_comment'),
)
