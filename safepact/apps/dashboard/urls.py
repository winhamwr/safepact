from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^homeowner/$",
        direct_to_template,
        {"template": "dashboard/homeowner.html"},
        name="dashboard_homeowner"),
    url(r"^contractor/$",
        direct_to_template,
        {"template": "dashboard/contractor.html"},
        name="dashboard_contractor"),
)
