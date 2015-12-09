from django import forms

# Forms

# Used to transport login information to a view
class LoginForm(forms.Form):
    email = forms.EmailField()
    pin = forms.IntegerField()

class MessageForm(forms.Form):
    msg = forms.CharField(max_length=160)
    list = forms.CharField(max_length=50)