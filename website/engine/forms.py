#-*- coding:utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.forms import ModelForm

from .models import Shop, Product, New
from .user import User

from fullcalendar.models import CalendarEvent

class MyForm(ModelForm):
    shop = None

    def save(self, commit=True):
        try:
            object_ = super(MyForm, self).save(commit=False)
            if self.shop:
                object_.shop = self.shop
            if commit:
                object_.save()
            self.shop = None
            return object_
        except Exception:
           raise forms.ValidationError(u'')

class EventForm(MyForm):
    class Meta:
        model = CalendarEvent
        exclude = ('shop',)

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        exclude = ()

class ProductForm(MyForm):
    class Meta:
        model = Product
        exclude = ('shop',)

class NewForm(MyForm):
    body = forms.CharField(label=u'内容',widget=forms.Textarea(attrs={'class': 'editor','placeholder':u'请在此输入内容'}))
    class Meta:
        model = New
        exclude = ('shop',)

class LoginForm(forms.Form):
    username = forms.CharField(label=u'用户名')
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput)

    class Meta:
        form_model = User
        field = ('name', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)    
        self.user_cache = None

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache  = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(u'用户名或者密码不正确')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'用户已被锁定')
            else:
                if not self.user_cache.is_admin and not self.user_cache.is_store:
                    raise PermissionDenied()

        return self.cleaned_data

    def get_user(self):
        return self.user_cache

class RegisterForm(forms.Form):
    username = forms.CharField(label=u'用户名')
    email = forms.EmailField(label=u'电子邮箱')
    password1 = forms.CharField(label=u'密码',  widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'确认密码' ,widget=forms.PasswordInput)

    def __init__(self, *args, **kw):
        super(RegisterForm, self).__init__(*args, **kw)    
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not username or not email or not password1 or not password2:
            raise forms.ValidationError(u'请将信息填写完整')
        elif password1 != password2:
            raise forms.ValidationError(u'两次输入的密码不一致')

        User.objects.create_user(name=username,
                                                    email=email,
                                                    password=password1)
        return self.cleaned_data
