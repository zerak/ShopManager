# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from engine.models import Shop

class CalendarEvent(models.Model):
    """The event set a record for an 
    activity that will be scheduled at a 
    specified date and time. 
    
    It could be on a date and time 
    to start and end, but can also be all day.
    
    :param title: Title of event
    :type title: str.
    
    :param start: Start date of event
    :type start: datetime.
    
    :param end: End date of event
    :type end: datetime.
    
    :param all_day: Define event for all day
    :type all_day: bool.
    """
    title = models.CharField(u'标题', blank=True, max_length=200)
    start = models.DateTimeField(u'起始时间')
    end = models.DateTimeField(u'结束时间')
    all_day = models.BooleanField(u'全日事件', default=False)
    shop = models.ForeignKey(Shop, verbose_name=u'商户ID')

    class Meta:
        verbose_name = u'事件'
        verbose_name_plural = u'事件'

    def __unicode__(self):
        return self.title
