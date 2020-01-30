from django import forms


class CreateNewFollower(forms.Form):
    maili = forms.EmailField()
