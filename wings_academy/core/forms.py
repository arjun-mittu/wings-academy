from django import forms
class cmtform(forms.Form):
    body=forms.CharField(required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
        'rows':'3'
    }))