from django.conf.urls.defaults import *

urlpatterns = patterns('',    
    url(r'^$', 'flag.views.falg', name="flag"),
)