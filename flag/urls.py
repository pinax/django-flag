from django.conf.urls.defaults import *
from django.views.generic import TemplateView


urlpatterns = patterns("",
    url(r"^$", "flag.views.flag", name="flag"),
    url(r'^thank_you', TemplateView.as_view(template_name="flag/thank_you.html"), name='flag-reported'),
)