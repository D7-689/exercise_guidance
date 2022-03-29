from django.shortcuts import render, redirect           
from django.contrib.auth import authenticate, login, logout  
from django.conf import settings
from .forms import UserCreationForm, FaceAuthenticationForm, ProfileUpdateForm,UserUpdateForm, defaultAuthenticationForm ,ChangePasswordform
from .authenticate import FaceIdAuthBackend 
from .utils import prepare_image 
from django.contrib import messages

# Import password_reset
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
import string
from django.contrib.auth.hashers import make_password


def loginpage(request):

    if request.method == "POST":
        form = defaultAuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)

        if user is not None:
             if user.is_active:
                login(request,user)
                return redirect('home')

        else:
            messages.info(request,'Incorrect username or password', extra_tags='login')            #remark orginal is [message.info]
            return redirect('login')

    context = {}
    return render(request, 'webpage/loginpage.html',context)

def register(request):
    if  request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)

        if form.is_valid():     #if the form is valid then
            form.save()         #save the form information
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password) #run authenticate.py 入面function
            messages.success(request,'Account was created for ' + username)
            login(request, user)
            return redirect('login')    
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'webpage/registerpage.html', context)

def face_login(request):
    if request.method == 'POST':
        form = FaceAuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            face_image = prepare_image(form.cleaned_data['image'])

            face_id = FaceIdAuthBackend() #run the class inside authenticate.py 
            user = face_id.authenticate(username=username,password=None,face_id=face_image)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username, password or face id didn't match.", extra_tags='facelogin_message')
                return redirect('facelogin')
    else:
        form = FaceAuthenticationForm()

    context = {'form': form}
    return render(request, 'webpage/facelogin.html', context)

def homepage(request):
    return render(request, 'webpage/homepage.html')

def logoutpage(request): #Seems work of the logout function
    if request.method == 'POST':
        logout(request)
    return redirect('login')

    # logout(request)
    # return render(request, "django_two_factor_face_auth/loginpage.html")

def profilepage(request):           #profile page that allow user update information
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request,"webpage/profile.html", context)

def password_reset_page(request): 
  
    if request.method == "GET":
        return render(request, "webpage/forget_password.html")
    else:
        username = request.POST.get("username")
        count = User.objects.filter(username=username).count()
        if count == 1:
            email = User.objects.get(username=username).email
            email_part = email[3:]

            # generate password,length = 8, letters and digits
            random_password = ''.join(random.sample(string.ascii_letters + string.digits, 8))

            # update password, hash password
            password = make_password(random_password)
            User.objects.filter(username=username).update(password=password)

            # send email
            subject = "Password reset notification"
            message = "Your username " + username + " 's password is changed into " + random_password
            sender = settings.EMAIL_HOST_USER
            recipient = [email]
            send_mail(
                subject,
                message,
                sender,
                recipient
            )
            return render(request, "webpage/forget_password.html", {"forget_password_tips": "Password is sent to *****" + email_part + " , please check your inbox or junk box."})
        else:
            return render(request, "webpage/forget_password.html", {"forget_password_tips": username + " is not exsit!"})

def dashboard(request):
    return render(request, 'webpage/dashboard.html')

# Change password page
def ChangePasswordPage(request):
    if request.method == 'GET':
        form = ChangePasswordform()
        return render(request, 'webpage/changepassword.html',{'form': form})

    else:
        form = ChangePasswordform(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return redirect('home')
            else:
                return render(request, 'webpage/changepassword.html',{'form': form,'oldpassword_is_wrong':True})
        else:
            return render(request, 'webpage/changepassword.html',{'form': form})
