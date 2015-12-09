from django.shortcuts import render
from forms import RegistrationForm, ConfirmationForm
from django.template.context_processors import csrf
import ViewLogic

# Create your views here.
def register(request):
    context = {}
    context['lists'] = ViewLogic.getListNames()
    context['active'] = ViewLogic.getActiveStatus()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first = str(form.cleaned_data['first'])
            last = str(form.cleaned_data['last'])
            phone = int(form.cleaned_data['phone'])
            lists = str(form.cleaned_data['lists'])
            ViewLogic.addUser(first, last, phone, lists)
            context['first'] = first
            context['last'] = last
            context['phone'] = phone
            context['lists'] = ViewLogic.getUserLists(first, last, phone)
            return render(request, 'ConfirmationPage.html', context)
    else:
        return render(request, 'RegistrationPage.html', context)

def confirm(request):
    context = {}
    if request.POST:
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            first = str(form.cleaned_data['first'])
            last = str(form.cleaned_data['last'])
            phone = int(form.cleaned_data['phone'])
            ViewLogic.activateUser(first, last, phone)
            context['first'] = first
            context['last'] = last
            context['phone'] = phone
            context['done'] = True
            return render(request, 'ConfirmationPage.html', context)
        else:
            return render(request, 'AddTokens.html', context)