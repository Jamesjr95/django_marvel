from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = '__all__'


        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'style':'font-style:italic'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'style':'font-style:italic'}),
        }

class UserAuthForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password']