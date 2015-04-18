#-*- coding:utf-8 -*-
from django.db import models
from shop.models import Shop

# Create your models here.
class New(models.Model):
    title = models.CharField(u'标题', max_length=100)
    body = models.TextField(u'内容')
    pic = models.ImageField(u'图片', upload_to='Public/new/new_pic/',
                                                        blank=True)
    add_date = models.DateField(u'日期',auto_now_add=True)
    shop = models.ForeignKey(Shop, default=None,
                                                                verbose_name=u'商户')

    def __unicode__(self):
        return self.title
