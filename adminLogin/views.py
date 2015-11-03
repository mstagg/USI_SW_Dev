from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.template.context_processors import csrf
from django import forms
from models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='password', max_length=100)

# Create your views here.

def adminLogin(request):
	context = {}
	context.update(csrf(request))

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = str(form.cleaned_data['username'])
			password = str(form.cleaned_data['password'])
			results = User.objects.filter(user_name = username, password = password, is_admin = True)
			if len(results) > 0:
				request.session['name'] = str(results.values_list('first_name', flat = True).get())
				request.session.set_expiry(600)
				context['name'] = request.session['name']
				context['failed'] = False
				template = loader.get_template('AdminManagement.html')
				data = RequestContext(request, context)
				response = HttpResponse(template.render(data))
				return HttpResponse(template.render(data))
			else:
				context['failed'] = True
				template = loader.get_template('AdminSignInPage.html')
				data = RequestContext(request, context)
				response = HttpResponse(template.render(data))
				return HttpResponse(template.render(data))
		else:
			template = loader.get_template('AdminSignInPage.html')
			data = RequestContext(request, context)
			response = HttpResponse(template.render(data))
			return HttpResponse(template.render(data))
	elif 'name' in request.session:
		request.session.set_expiry(600)
		context['name'] = request.session['name']
		template = loader.get_template('AdminManagement.html')
		data = RequestContext(request, context)
		response = HttpResponse(template.render(data))
		return HttpResponse(template.render(data))
	else:
		template = loader.get_template('AdminSignInPage.html')
		data = RequestContext(request, context)
		response = HttpResponse(template.render(data))
		return HttpResponse(template.render(data))
