#-*- coding:utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from engine.models import User

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='密码确认',
        widget=forms.PasswordInput,
    )
    class Meta:
        model = User
        fields = ('name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"

    def clean_password(self):
        return self.initial["password"]

class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('name', 'created_at', 'email', 'is_delete', 'is_admin','is_store')
    search_fields = ('name', 'email')
    list_filter = ('is_admin',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'avatar',)}),
        (u'个人信息', {'fields': ('created_at', 'updated_at')}),
        (
            u'token信息',
            {
                'fields': ('access_token', 'refresh_token', 'expires_in')
            }
        ),
        (u'权限', {'fields': ('is_delete', 'is_admin', 'is_store','is_active')}),
        (u'登录信息', {'fields': ('last_login',)}),
        (u'店铺', {'fields': ('own_shop',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('name', 'email', 'password1', 'password2'),
            }
        ),
    )
    ordering = ('created_at',)
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)