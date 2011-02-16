from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mockups.views',
    url(r'^contractor/signup$', 'contractor_signup'),
    url(r'^homeowner/signup$', 'homeowner_signup'),
)
