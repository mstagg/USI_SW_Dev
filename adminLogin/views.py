from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django import forms
from models import User, List

# Forms
# TODO: move into their own py file

# Used to transport login information to a view
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='password', max_length=100)

# Used to transport a new logo image to a view
class UploadLogo(forms.Form):
    file = forms.FileField()

class CreateNewList(forms.Form):
    newListName = forms.CharField(max_length = 50)

# Views

# Admin login page
def adminLogin(request):
    context = {}
    context.update(csrf(request))

    # If received a POST request...
    if request.POST:
        form = LoginForm(request.POST)
        # If login form has legitimate data...
        if form.is_valid():
            u = str(form.cleaned_data['username'])
            p = str(form.cleaned_data['password'])
            # If login credentials exist in database...
            # Return the management page
            if adminExists(u, p):
                request.session['name'] = getName(u, p)
                request.session['admin'] = True
                request.session.set_expiry(600)
                context['name'] = request.session['name']
                context['failed'] = False
                return render(request, 'AdminManagement.html', context)
            # If login credentials do NOT exist...
            # Return the sign in page
            else:
                context['failed'] = True
                return render(request, 'AdminSignInPage.html', context)
        # If login form did NOT contain legitimate data...
        # Return the sign in page
        else:
            return render(request, 'AdminSignInPage.html', context)

    # If received any other request...
    else:
        # If a user is currently logged in AND is an admin...
        # Return the management page
        if 'admin' in request.session:
            request.session.set_expiry(600)
            context['name'] = request.session['name']
            return render(request, 'AdminManagement.html', context)
        # If no admin user is currently logged in...
        # Return the sign in page
        else:
            return render(request, 'AdminSignInPage.html', context)

def adminLogout(request):
    request.session.flush()
    return redirect('adminLogin.views.adminLogin')

# Update the logo page
def updateLogo(request):
    context = {}
    context.update(csrf(request))

    # If a user is logged in AND is an admin...
    if 'admin' in request.session:
        # If request is a POST request
        if request.POST:
            request.session.set_expiry(600)
            form = UploadLogo(request.POST, request.FILES)
            # If login form has legitimate data...
            # Replace logo.jpg with new files and return update logo page
            if form.is_valid():
                if replaceLogo(request.FILES['file']):
                    context['success'] = True
                    return render(request, 'UpdateLogo.html', context)
                else:
                    context['success'] = False
                    return render(request, 'UpdateLogo.html', context)
        # If received any other request...
        # Return the update logo page
        else:
            request.session.set_expiry(600)
            return render(request, 'UpdateLogo.html', context)
    # If user is not logged in or not an admin...
    # Redirect to the admin sign in page
    else:
        return redirect('adminLogin.views.adminLogin')

# Allows user to manage mailing lists
def manageLists(request):
    context = {}
    context.update(csrf(request))
    # If user is logged in AND is an admin...
    if 'admin' in request.session:
        request.session.set_expiry(600)
        context['mailingLists'] = getListNames()
        # If request is POST...
        if request.POST:
            form = CreateNewList(request.POST)
            # If login form has legitimate data...
            # Add a new List model with the name from the form
            if form.is_valid():
                n = str(form.cleaned_data['newListName'])
                newList = List(name = n, size = 0)
                newList.save()
                context['mailingLists'] = getListNames()
                return render(request, 'ManageLists.html', context)
        # If request is GET...
        else:
            return render(request, 'ManageLists.html', context)
    # If admin login has expired, return to login page
    else:
        return redirect('adminLogin.views.adminLogin')

def accountInfo(request):
    context = {}
    if 'admin' in request.session:
        request.session.set_expiry(600)
        return render(request, 'AccountInformation.html', context)
    else:
       return redirect('adminLogin.views.adminLogin')

def addTokens(request):
    context = {}
    if 'admin' in request.session:
        request.session.set_expiry(600)
        return render(request, 'AddTokens.html', context)
    else:
       return redirect('adminLogin.views.adminLogin')


# Auxiliary functions

# Takes username and password and returns the user's first name
def getName(usr, pwd):
    results = User.objects.filter(user_name = usr, password = pwd, is_admin = True)
    return str(results.values_list('first_name', flat = True).get())

# Takes username and password and searches database for an admin account
def adminExists(usr, pwd):
    results = User.objects.filter(user_name = usr, password = pwd, is_admin = True)
    if(len(results) > 0):
        return True
    else:
        return False

def getListNames():
    results = List.objects.filter()
    r = results.values_list('name', flat = True)
    return r

# TODO: return false if file type is not an image
# Replaces the site logo with the file f
def replaceLogo(f):
    try:
        with open('evvdayschool/static/res/logo.jpg', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return True
    except:
        return False