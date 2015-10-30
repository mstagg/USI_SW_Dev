from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext

# Create your views here.

def admin(request):
	context = {}

	template = loader.get_template('AdminSignInPage.html')
	data = RequestContext(request, context)
	response = HttpResponse(template.render(data))
	
	#request.session['test1'] = '12345'
	
	return HttpResponse(template.render(data))
	#response = render_to_response("AdminSignInPage.html")
	#return response
