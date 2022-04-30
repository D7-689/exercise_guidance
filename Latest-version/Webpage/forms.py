from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserFaceImage
from .utils import base64_file
from .models import Learner,User_Weight_Height

class UserCreationForm(UserCreationForm):
    image = forms.CharField(widget=forms.HiddenInput())     #hidden tag image

    email = forms.EmailField(              
                label="Email address",
                widget=forms.EmailInput(attrs={'class':'text_field', 'type':'type'}),
            )  
    class Meta:
        model = User
        fields = ("username",'email', "password1", "password2")     

    def save(self, commit=True):
        if not commit:            
            raise NotImplementedError("Can't create User and UserFaceImage without database save")
        user = super(UserCreationForm, self).save(commit=True)                                                  #https://stackoverflow.com/questions/34849328/extending-usercreationform-password-not-saved
        image = base64_file(self.data['image'])
        face_image = UserFaceImage(user=user, image=image)
        face_image.save()
        return user

# A Specific authentication form that use for face login 
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


class User_Weight_HeightUpdateForm(forms.ModelForm):
    class Meta:
        model = User_Weight_Height
        fields = ['height','weight','age','gender'] 



# Create a form that allow user change the password by themselve
class ChangePasswordform(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter the oldpassword'},
        widget=forms.PasswordInput(),
    ) 
    newpassword1 = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter the newpassword'},
        widget=forms.PasswordInput(),
    )
    newpassword2 = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter the newpassword again'},
        widget=forms.PasswordInput(),
     )

