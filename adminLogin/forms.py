from django import forms

# Forms

# Used to transport login information to a view
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(label='password', max_length=100)


# TODO: CHANGE NAME TO REFLECT GENERIC FILE UPLOAD
# Used to transport a file from a client to the view via a form
class UploadLogo(forms.Form):
    file = forms.FileField()


# TODO: CHANGE NAME TO REFLECT GENERIC CHARFIELD UPLOAD
# Used to transport a string from a client to the view via a form
class ListForm(forms.Form):
    name = forms.CharField(max_length = 50)


# Used to transport all relevant to create a new User
class CreateNewSender(forms.Form):
    email = forms.EmailField()
    firstName = forms.CharField(max_length = 50)
    lastName = forms.CharField(max_length = 50)
    pin = forms.IntegerField()


# TODO: CHANGE NAME TO REFLECT GENERIC EMAIL UPLOAD
# Used to transport an email from a client to the view via a form
class DeleteSender(forms.Form):
    email = forms.EmailField()