from django import forms

# Forms

# Used to transport login information to a view
class RegistrationForm(forms.Form):
    phone = forms.IntegerField()
    first = forms.CharField(max_length=50)
    last = forms.CharField(max_length=50)
    code = forms.CharField(max_length=8, required=False)
    lists = forms.CharField(max_length=250)

class ConfirmationForm(forms.Form):
    phone = forms.IntegerField()
    first = forms.CharField(max_length=50)
    last = forms.CharField(max_length=50)

class RemovalForm(forms.Form):
    phone = forms.IntegerField()