from django import forms
# from rufferuser.models import RufferUser


class PostImageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'exampleFormControlTextarea1',
            'rows': "3"
        }
    ))
    image = forms.ImageField()
