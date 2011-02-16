from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from forms import ContractorSignupForm

def index(request):
    context = {}
    return render_to_response("mockups/index.html", context,
                              context_instance=RequestContext(request))
                              
def contractor_signup(request):
    form = ContractorSignupForm()
    context = {'form' : form}
    return render_to_response("mockups/contractor_signup.html", context,
                              context_instance=RequestContext(request))
                              
def homeowner_signup(request):
    context = {}
    return render_to_response("mockups/homeowner_signup.html", context,
                              context_instance=RequestContext(request))
