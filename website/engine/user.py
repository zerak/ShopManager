#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from engine.models import Shop
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("Users must have an Email address")
        user = self.model(
            name=name,
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(name, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(u'呢称',max_length=52, unique=True)
    email = models.EmailField(u'E-mail',max_length=100, unique=True, 
                                                                    blank=True)
    avatar = models.URLField(u'头像',blank=True)
    created_at = models.DateTimeField(u'创建时间',auto_now_add=True)
    updated_at = models.DateTimeField(u'修改时间',auto_now=True)
    is_delete = models.BooleanField(u'是否删除',default=False)
    is_active = models.BooleanField(u'是否活跃',default=True)
    is_admin = models.BooleanField(u'是否管理员',default=False)
    is_store = models.BooleanField(u'是否商户',default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(default=0)
    own_shop = models.OneToOneField(Shop, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'
        ordering = ('created_at',)

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.email

    def get_short_name(self):
      return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kw):
        if self.own_shop is not None:
            self.is_store = True
        else:
            self.is_store = False
        super(User, self).save(*args, **kw)