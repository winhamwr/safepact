from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

def index(request):
    context = {}
    return render_to_response("mockups/index.html", context,
                              context_instance=RequestContext(request))
                              

