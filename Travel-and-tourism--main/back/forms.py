from django import forms
from .models import *

from .forms import *


class EmpRegisForm(forms.ModelForm):
    FirstName = forms.CharField(widget=forms.TextInput({"placeholder":"First Name"}))
    LastName = forms.CharField(widget=forms.TextInput({"placeholder":"Last Name"}))
    email = forms.EmailField(widget=forms.TextInput({"placeholder":"Enter your Email"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder":"Password Please"}),min_length=1, max_length=16)
    Confirmpassword = forms.CharField(label='password(again)', widget=forms.PasswordInput({"placeholder":"Password Please"}),min_length=1, max_length=16)
    class Meta:
        model = Sign
        fields ='__all__'
    
# #form for login page
class SignInForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput({"placeholder":"Enter your Email"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder":"Password Please"}),min_length=1, max_length=16)
    class Meta:
        model = Sign
        fields =['email','password']

class insertdata(forms.ModelForm):
    class Meta():
        model = contact_me
        fields ='__all__'