from django import forms
from django.core import validators
from backend.models import Vegetable



def phone_no(phone_no):
    p = phone_no
    if len(p)!=10:
        raise forms.ValidationError('phone number is not correct')
    return p

class RegisterForm(forms.Form):
    username  = forms.CharField(validators=[validators.MaxLengthValidator(6)])
    phone_no = forms.CharField(validators=[phone_no])
    pwd = forms.CharField()
    # def clean_phone_no(self):
    #     p = self.cleaned_data['phone_no']
    #     if len(p)!=10:
    #         raise forms.ValidationError('phone number is not correct')
    #     return p

    def clean_pwd(self):
        p = self.cleaned_data['pwd']
        l = 0
        u =0
        d = 0
        e = 0
        upper =False
        lower =False
        digit =False
        special =False
        if len(p) >5 and len(p)<15:
            for i in p:
                if i.isupper():
                    u = u+1
                elif i.islower():
                    l= l +1
                elif i.isdigit():
                    d=d+1
                elif i == "@":
                    e = e+1
            if (u>=1):
                upper = True
            else:
                raise forms.ValidationError("upper case")

            if (l>=1):
                lower = True
            else:
                raise forms.ValidationError("lower case")
            if (d>=1):
                digit = True
            else:
                raise forms.ValidationError("digit")
            if (e>=1):
                special = True
            else:
                raise forms.ValidationError("@")
            
            if (lower==upper==digit==special==True):
                return p
            else:
                raise forms.ValidationError('password is incorrect')
            
        else:
            raise forms.ValidationError("length must be greater then 5 and less then 15")
        

class LoginForm(forms.Form):
    username = forms.CharField()
    pwd = forms.CharField()


class VegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = '__all__'


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_no = forms.CharField(max_length=100)
    pincode = forms.IntegerField()
    state = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    address = forms.Textarea()
    quantity = forms.IntegerField()
    amount = forms.IntegerField()

    