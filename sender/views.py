from django.shortcuts import render, redirect
from django.template.context_processors import csrf
import ViewLogic
from forms import LoginForm

# Create your views here.
# Allows user to log in to the admin management site
def senderLogin(request):
    context = {}
    context.update(csrf(request))

    # If received a POST request...
    if request.POST:
        form = LoginForm(request.POST)
        # If login form has legitimate data...
        if form.is_valid():
            u = str(form.cleaned_data['email'])
            p = str(form.cleaned_data['pin'])
            # If login credentials exist in database...
            # Return the management page
            if ViewLogic.senderExists(u, p):
                request.session['email'] = u
                request.session['sender'] = True
                request.session.set_expiry(600)
                context['email'] = request.session['email']
                context['lists'] = ViewLogic.getSenderLists(u)
                context['failed'] = False
                return render(request, 'SendMessagePage.html', context)

            # If login credentials do NOT exist...
            # Return the sign in page
            else:
                context['failed'] = True
                return render(request, 'SenderSignInPage.html', context)

        # If login form did NOT contain legitimate data...
        # Return the sign in page
        else:
            return render(request, 'SenderSignInPage.html', context)

    # If received any other request...
    else:
        # If a user is currently logged in AND is an admin...
        # Return the management page
        if 'sender' in request.session:
            request.session.set_expiry(600)
            context['email'] = request.session['email']
            context['lists'] = ViewLogic.getSenderLists(context['email'])
            return render(request, 'SendMessagePage.html', context)

        # If no admin user is currently logged in...
        # Return the sign in page
        else:
            return render(request, 'SenderSignInPage.html', context)

# Handles logout procedures
def senderLogout(request):
    request.session.flush()
    return redirect('sender.views.senderLogin')