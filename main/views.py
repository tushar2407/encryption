from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout,
)
from services.decrypt import decrypt
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
# Create your views here.
from services.encrypt import encrypt, encrypt1
from services.decrypt import decrypt, decrypt1
from django.contrib.auth.models import User
from main.forms import File_upload
from main import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class Account(ListView):
    model=models.File
    template_name='main/account.html'
    context_object_name = 'files'

    def post(self, request):
        myfile = request.FILES['myfile']
        fs= FileSystemStorage()
        filename=fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        context = {
            "uploaded_file_url": uploaded_file_url
        }
        print(filename)
        print(uploaded_file_url)
        return render(request,'main/account.html', context)

class Index(LoginView):
    template_name='main/index.html'
    redirect_authenticated_user= True
class Logout(Logout):
    next_page='/'
    #return HttpResponseRedirect('')
def base(request):
    return render(request,'base.html')
#def index(request):
 #   return render(request,'main/index.html')
def page1(request):
    return render(request,'main/page1.html')
def account(request):
    return render(request, 'main/account.html')
class Encrypt(TemplateView):
    template_name='main/encrypt.html'
    def post(self, request):
        if 'text' in request.POST:
            content = request.POST['text']
            encrypted_content=encrypt(content)

        else:
            file_path = request.POST['text2']
            encrypted_content=encrypt1(file_path)

        context={
            "encrypted_content":encrypted_content
        }
        return render(request, self.template_name,context)
class Decrypt(TemplateView):
    template_name='main/decrypt.html'
    def post(self,request):
        #content = request.POST['text1']
        #file_path=request.POST['text3']

        if 'text1' in request.POST:
            content=request.POST['text1']
            decrypted_content=decrypt(content)
        else:
            file_path=request.POST['text3']
            decrypted_content=decrypt1(file_path)

        context={
            "decrypted_content":decrypted_content
        }
        return render(request,self.template_name,context)
'''
        class Encrypt_file(TemplateView):
    template_name='main/encrypt.html'
    def post(self,request):
        file_path = request.POST['text2']
        encrypted_content=encrypt1(file_path)
        context={
            "encrypted_content":encrypted_content
        }
        return render(request, self.template_name,context)
    '''
'''class Decrypt_file(TemplateView):
    template_name='main/decrypt.html'
    def post(self,request):
        file_path=request.POST['text3']
        decrypted_content=decrypt1(file_path)
        context={
            "decrypted_content":decrypted_content
        }
        return render(request,self.template_name,context)
'''
class SignUp(LoginView):
    template_name='main/signup.html'
    def post(self,request):
        username=request.POST['username']
        email=request.POST['user']
        password=request.POST['password']
        re_password=request.POST['re_password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        context={
            "username":username,
            "password":password, 
            "email":email,
            "first_name":first_name
        }
        if password == re_password:
            user=User.objects.create_user(username,first_name=first_name,email=email,password=password)
            user.save()
            redirect_authenticated_user= True
            return render(request, self.template_name, context)
        else :
            return HttpResponseBadRequest('Paswords do not match')
