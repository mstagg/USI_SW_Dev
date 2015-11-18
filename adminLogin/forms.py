from django import forms

# Forms

# Used to transport login information to a view
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(label='password', max_length=100)

# Used to transport a new logo image to a view
class UploadLogo(forms.Form):
    file = forms.FileField()

class ListForm(forms.Form):
    name = forms.CharField(max_length = 50)

class CreateNewSender(forms.Form):
    email = forms.EmailField()
    firstName = forms.CharField(max_length = 50)
    lastName = forms.CharField(max_length = 50)
    pin = forms.IntegerField()

class DeleteSender(forms.Form):
    email = forms.EmailField()