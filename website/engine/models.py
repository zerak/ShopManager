#-*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Shop(models.Model):
    name = models.CharField(u'名称', max_length=100, unique=True)
    location = models.CharField(u'位置', max_length=100, unique=True)
    introduction = models.TextField(u'简介', blank=True)
    logo = models.ImageField(u'图片', upload_to='Public/shop/shop_logo/',blank=True)
    area_id = models.IntegerField(u'区域id',blank=True)
    add_date = models.DateTimeField(u'日期',auto_now_add=True)

    def __unicode__(self):
        return self.name

    @property
    def shop_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_detail', kwags={'pk', self.pk})

class Product(models.Model):
    PRODUCT_TYPES = (
        ('Food', '食品'),
        ('Daily', '日用品'),
    )
    name = models.CharField(u'商品名称',max_length=100)
    image =  models.ImageField(u'商品图片',upload_to='Public/shop/products/',
                                                                    blank=True)
    product_type = models.CharField(u'商品类型',max_length=10,
                                                                choices=PRODUCT_TYPES,
                                                                blank=True,)
    price = models.FloatField(u'商品价格')
    shop = models.ForeignKey(Shop, verbose_name=u'商户ID')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwags={'pk', self.pk})

class New(models.Model):
    title = models.CharField(u'标题', max_length=60)
    body = models.TextField(u'内容')
    add_date = models.DateTimeField(u'发布日期', auto_now_add=True)
    shop = models.ForeignKey(Shop, verbose_name=u'商户ID')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-add_date',)
