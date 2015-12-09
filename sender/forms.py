from django import forms

# Forms

# Used to transport login information to a view
class LoginForm(forms.Form):
    email = forms.EmailField()
    pin = forms.IntegerField()