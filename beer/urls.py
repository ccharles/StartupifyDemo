from django.conf.urls.defaults import *

urlpatterns = patterns('beer.views',
    # Examples:
    # url(r'^$', 'startupifydemo.views.home', name='home'),
    # url(r'^startupifydemo/', include('startupifydemo.foo.urls')),
    url(r'^brewery/(?P<brewery_id>\d+)/$', 'brewery'),
)
