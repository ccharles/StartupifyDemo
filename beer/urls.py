from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from beer.models import Brewery, Beer, Review, ReviewComment

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Review.objects.order_by('-date')[:5],
            context_object_name='latest_reviews',
            template_name='beer/index.html')),
    url(r'^brewery/$',
        ListView.as_view(
            queryset=Brewery.objects.order_by('name'),
            context_object_name='breweries',
            template_name='beer/breweries.html')),
    url(r'^brewery/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Brewery,
            template_name='beer/brewery.html')),
    url(r'^beer/$',
        ListView.as_view(
            queryset=Beer.objects.order_by('name'),
            context_object_name='beers',
            template_name='beer/beers.html')),
    url(r'^beer/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Beer,
            template_name='beer/beer.html')),
)

urlpatterns += patterns('beer.views',
    url(r'^review/(?P<review_id>\d+)/$', 'review'),
    url(r'^review/(?P<review_id>\d+)/comment/$', 'review_comment'),
)
