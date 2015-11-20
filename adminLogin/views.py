from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from models import User, List
from forms import LoginForm, UploadLogo, ListForm, CreateNewSender, DeleteSender
import ViewLogic
from django.http import HttpResponse

# Views

# Allows user to log in to the admin management site
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
            if ViewLogic.adminExists(u, p):
                request.session['name'] = ViewLogic.getName(u, p)
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


# Handles logout procedures, only accepts POST
def adminLogout(request):
    request.session.flush()
    return redirect('adminLogin.views.adminLogin')


# TODO: ADD CODE TO HANDLE INVALID FORMS
# Allows user to update the current site logo
def updateLogo(request):
    context = {}
    context.update(csrf(request))

    # If a user is logged in AND is an admin...
    if 'admin' in request.session:
        request.session.set_expiry(600)
        # If request is a POST request...
        if request.POST:
            form = UploadLogo(request.POST, request.FILES)
            # If form has legitimate data...
            # Replace logo.jpg with new files and return update logo page
            if form.is_valid():
                if ViewLogic.replaceLogo(request.FILES['file']):
                    context['success'] = True
                    return render(request, 'UpdateLogo.html', context)

                else:
                    context['success'] = False
                    return render(request, 'UpdateLogo.html', context)
            # If form did NOT contain legitimate data...
            # Return the update logo page with error prompt
            else:
                pass
        # If received any other request...
        # Return the update logo page
        else:
            return render(request, 'UpdateLogo.html', context)

    # If user is not logged in or not an admin...
    # Redirect to the admin sign in page
    else:
        return redirect('adminLogin.views.adminLogin')


# TODO: PREVENT ADDING LISTS WITH THE SAME NAME
# Allows user to create, edit, and delete mailing lists
def manageLists(request):
    context = {}
    context.update(csrf(request))

    # If user is logged in AND is an admin...
    if 'admin' in request.session:
        request.session.set_expiry(600)
        context['mailingLists'] = ViewLogic.getListNames()
        # If request is POST...
        if request.POST:
            form = ListForm(request.POST)
            # If form has legitimate data...
            # Add a new List model with the name from the form
            if form.is_valid():
                n = str(form.cleaned_data['name'])
                newList = List(name = n, size = 0)
                newList.save()
                context['mailingLists'] = ViewLogic.getListNames()
                return render(request, 'ManageLists.html', context)

            # If form did NOT contain legitimate data...
            # Return the manage lists page with error prompt
            else:
                context['failed'] = True
                return render(request, 'ManageLists.html', context)

        # If request is GET...
        else:
            return render(request, 'ManageLists.html', context)

    # If admin login has expired, return to login page
    else:
        return redirect('adminLogin.views.adminLogin')


def manageIndividualList(request):
    context = {}
    if 'admin' in request.session:
        request.session.set_expiry(600)
        context['listName'] = request.GET.get('q', '')
        context['listUsers'] = ViewLogic.getListUsers(context['listName'])
        context['listSize'] = len(context['listUsers'])
        return render(request, 'ManageIndividualList.html', context)
    else:
        return redirect('adminLogin.views.adminLogin')


# Handles the deletion of lists, only accepts POST
def deleteList(request):
    # If admin is logged in and request is POST...
    # Delete the list that shares a name with the name from the form
    if 'admin' in request.session and request.POST:
        request.session.set_expiry(600)
        form = ListForm(request.POST)
        if form.is_valid():
            n = str(form.cleaned_data['name'])
            List.objects.filter(name = n).delete()
            return redirect('adminLogin.views.manageLists')


# TODO: PREVENT ADDING USERS WITH THE SAME EMAIL
# Allows user to create, edit, and delete users with sender permissions
def manageSenders(request):
    context = {}
    context.update(csrf(request))

    # If admin is logged in...
    if 'admin' in request.session:
        request.session.set_expiry(600)
        context['emailList'] = ViewLogic.getSenderEmails()
        # If request type is POST...
        if request.POST:
            form = CreateNewSender(request.POST)
            # If form has legitimate data...
            # Add a new User model with the information from the form
            if form.is_valid():
                e = str(form.cleaned_data['email'])
                f = str(form.cleaned_data['firstName'])
                l = str(form.cleaned_data['lastName'])
                p = int(form.cleaned_data['pin'])
                newSender = User(user_name = ViewLogic.generateUserName(f, l),
                                 password = "",
                                 email = e,
                                 pin = p,
                                 is_admin = False,
                                 is_sender = True,
                                 first_name = f,
                                 last_name = l)
                newSender.save()
                context['emailList'] = ViewLogic.getSenderEmails()
                return render(request, 'ManageSenders.html', context)

            # If form did NOT contain legitimate data...
            # Return the manage lists page with error prompt
            else:
                context['failed'] = True
                return render(request, 'ManageSenders.html', context)

        # If request is not POST...
        else:
            return render(request, 'ManageSenders.html', context)

    # If admin login has expired, return to login page
    else:
        return redirect('adminLogin.views.adminLogin')


# Handles the deletion of sender users, only accepts POST
def deleteSender(request):
    # If admin is logged in and request is POST...
    # Delete the User that shares the email with the email from the form
    if 'admin' in request.session and request.POST:
        request.session.set_expiry(600)
        form = DeleteSender(request.POST)
        if form.is_valid():
            e = str(form.cleaned_data['email'])
            User.objects.filter(email = e).delete()
            return redirect('adminLogin.views.manageSenders')

# TODO: IF FORM IS INVALID
def manageSenderLists(request):
    context = {}

    if 'admin' in request.session:
        request.session.set_expiry(600)
        if request.POST:
            form = ListForm(request.POST)
            if form.is_valid():
                context['senderEmail'] = request.GET.get('q', '')
                l = ViewLogic.stringToList(form.cleaned_data['name'])
                ViewLogic.addUserLists(context['senderEmail'], l)
                context['mailingLists'] = ViewLogic.getUserListOwnership(context['senderEmail'])
                context['success'] = True
                return render(request, 'ManageSenderLists.html', context)
                #return HttpResponse(str(ViewLogic.getUserListOwnership(context['senderEmail'])))
                #ViewLogic.updateSenderLists(lists);
                #return render(request, 'ManageSenderLists.html', context)
            else:
                pass
        else:
            context['senderEmail'] = request.GET.get('q', '')
            context['mailingLists'] = ViewLogic.getUserListOwnership(context['senderEmail'])
            return render(request, 'ManageSenderLists.html', context)


#TODO: ADD FUNCTIONALITY
def accountInfo(request):
    context = {}
    if 'admin' in request.session:
        request.session.set_expiry(600)
        return render(request, 'AccountInformation.html', context)
    else:
       return redirect('adminLogin.views.adminLogin')

#TODO: ADD FUNCTIONALITY
def addTokens(request):
    context = {}
    if 'admin' in request.session:
        request.session.set_expiry(600)
        return render(request, 'AddTokens.html', context)
    else:
       return redirect('adminLogin.views.adminLogin')