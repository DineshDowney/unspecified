from django import forms

class FormClass(forms.Form):

    name= forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Your full name"}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder":"Your Email address"}))
    text= forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder":"Your message"}))
    
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Your username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder":"Your password"}))

class RegisterForm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Your Full name"}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder":"Your Email address"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder":"Set desired username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control","placeholder":"Set Password"}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class": "form-control","placeholder":"Type the password again"}))
    
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")
        if password2!= password:
            raise forms.ValidationError("Passwords must match")
        return data