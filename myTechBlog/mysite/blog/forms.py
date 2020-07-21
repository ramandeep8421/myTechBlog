from django import forms
from .models import Post, Comment , ContactFormModel,NewsLetterModel
from django.core import validators
from django.contrib.auth.models import User
from blog.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

#def check_for_H(value):
    #if value[0].lower != 'h':
        #raise forms.ValidationError("NAME NEEDS TO START WITH H/h")


class NewsLetter(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = '__all__'

        widgets = {
          'email':forms.TextInput(attrs ={'class':'form-control'})
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text','image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass form-control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            #'author': forms.TextInput(attrs={'class':'form-control'}),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model =  ContactFormModel
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs ={'class':'form-control'}),
            'email':forms.TextInput(attrs ={'class':'form-control'}),
            'text':forms.Textarea(attrs ={'class':'form-control'}),
        }
