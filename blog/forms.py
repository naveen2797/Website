from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Contact, Post
from django.utils.translation import gettext, gettext_lazy as _

class contactform(forms.ModelForm):
   class Meta:
      model = Contact
      fields = ['name','email','phone','desc']
      widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'})
        }
            
      labels = {'name':'Enter your Name','email':'Enter your Email','phone':'Enter your Phone Number','desc':'Enter your Message'}
      error_messages = {'name':{'required':'please enter your correct Name'},'email':{'required':'Enter Your correct email id'},'phone':{'requried':'Enter Your Correct Phone Number'}}




   

class signupfrom(UserCreationForm):

   password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}),label_suffix=' ')
   password2 = forms.CharField(label='Confrom_password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}),label_suffix=' ')
   class Meta:
      model = User
      fields = ['username','first_name','last_name','email']
      labels = {'email':'Email'}
      label_suffix=''
      widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
      }    

class LoginForm(AuthenticationForm):
   username = UsernameField(widget = forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}),label_suffix=' ')
   password = forms.CharField(label=_('password'),strip=False,widget = forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}),label_suffix=' ')


class PostFrom(forms.ModelForm):
      class Meta:
            model = Post
            fields = ['title','content','author','Slug']
            widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'Slug': forms.TextInput(attrs={'class':'form-control'})
            }
            labels = {'Slug':'Slug(please Mention titel Name again)'}


      
      
