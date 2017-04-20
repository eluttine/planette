from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib.staticfiles import views


urlpatterns = patterns(
    'api.views',
    url(r'^posts/$', 'post_list', name='post_list'),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^thumbnails/(?P<path>.*)$', views.serve),
    ]
