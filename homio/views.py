from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from homio import forms
from django.views.generic import ListView
from products.models import Product
import time
class product_list_view(ListView):
    context={}
    queryset=Product.objects.all()
    template_name='index.html'
    def get_context_data(self,*args,**kwargs):
        context=super(product_list_view,self).get_context_data(*args,**kwargs)
        print(context)
        context["title"]="Not logged in"
        if self.request.user.is_authenticated:
                context["title"]="Logged in"
                context['username']=self.request.user
        return context

def about_us(request):
    return render(request,"about.html")

def cart(request):
    return render(request,"cart.html")

def login_page(request):
    LForm=forms.LoginForm(request.POST or None)
    print("User logged in: "+str(request.user.is_authenticated))
    if LForm.is_valid():
        username=LForm.cleaned_data.get("username")
        password=LForm.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            print("Error")
            # No backend authenticated the credentials
    return render(request,"login.html",{'form_dic':LForm})

User=get_user_model()
def register_page(request):
    RForm=forms.RegisterForm(request.POST or None)
    if RForm.is_valid():
        print(RForm.cleaned_data)
        username=RForm.cleaned_data.get("username")
        password=RForm.cleaned_data.get("password")
        email=RForm.cleaned_data.get("email")
        new_user=User.objects.create_user(username,email,password)
        print(new_user)
        login_page(request)
    return render(request,"register.html",{'form_dic':RForm})