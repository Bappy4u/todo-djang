from django import forms


class ProfilesForm(forms.Form):
    bio_field = forms.CharField()
    img_field = forms.ImageField()