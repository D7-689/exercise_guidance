from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserFaceImage
from .utils import base64_file
from .models import Learner

class UserCreationForm(UserCreationForm):
    image = forms.CharField(widget=forms.HiddenInput())     #隱藏標籤 image

    email = forms.EmailField(              
                label="Email address",
                widget=forms.EmailInput(attrs={'class':'text_field', 'type':'type'}),
            )  
    class Meta:
        model = User
        fields = ("username",'email', "password1", "password2")     #張form 有三個variable 分別係username ,password1 同password2

    def save(self, commit=True):
        if not commit:            #如果没有提交  #可能呢度可以改self.errors (there validation is done 验证已经完成)
            raise NotImplementedError("Can't create User and UserFaceImage without database save")
        user = super(UserCreationForm, self).save(commit=True)          #https://stackoverflow.com/questions/34849328/extending-usercreationform-password-not-saved
        image = base64_file(self.data['image'])
        face_image = UserFaceImage(user=user, image=image)
        face_image.save()
        return user

# login 用
class FaceAuthenticationForm(AuthenticationForm):
    image = forms.CharField(widget=forms.HiddenInput())
    password = None

# User name and password
class defaultAuthenticationForm(AuthenticationForm):
    pass

class UserUpdateForm(forms.ModelForm):      # allow user to update the username,email and password
    email = forms.EmailField(
                label="Email address",
                widget=forms.TextInput(attrs={'class':'text_field', 'type':'type'}),
            )

    class Meta:
            model = User             
            fields = ['email']

class ProfileUpdateForm(forms.ModelForm):   # allow user to update the profile pic
    class Meta:
        model = Learner
        fields = ['name','phone','city','image'] 

# Create a form that allow user change the password by themselve
class ChangePasswordform(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label="Oldpassword",
        error_messages={'required': 'Please enter the oldpassword'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"",
            }
        ),
    ) 
    newpassword1 = forms.CharField(
        required=True,
        label="New password",
        error_messages={'required': 'Please enter the newpassword'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label="Re-enter new password",
        error_messages={'required': 'Please enter the newpassword again'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"",
            }
        ),
     )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("All the field must be filled in")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError("The new password and confirmation password do not match,please try again")
        else:
            cleaned_data = super(ChangePasswordform, self).clean()
        return cleaned_data
