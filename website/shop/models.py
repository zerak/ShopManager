#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPES = (
        ('Food', '食品'),
    )
    name = models.CharField(u'商品名称',max_length=100)
    image =  models.ImageField(u'商品图片',upload_to='Public/shop/products/',
                                                                    blank=True)
    product_type = models.CharField(u'商品类型',max_length=10,
                                                                choices=PRODUCT_TYPES,
                                                                blank=True,)
    price = models.FloatField(u'商品价格')

    def __unicode__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(u'名称', max_length=100, unique=True)
    location = models.CharField(u'位置', max_length=100, unique=True)
    introduction = models.TextField(u'简介', blank=True)
    logo = models.ImageField(u'图片', upload_to='Public/shop/shop_logo/',blank=True)
    area_id = models.IntegerField(u'区域id',blank=True)
    add_date = models.DateTimeField(u'日期',auto_now_add=True)
    products = models.ManyToManyField(Product,verbose_name=u'产品',blank=True)

    def __unicode__(self):
        return self.name

    @property
    def shop_name(self):
        return self.name

