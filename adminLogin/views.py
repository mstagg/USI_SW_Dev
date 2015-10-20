from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def admin(request):
	return render_to_response("AdminSignInPage.html")
