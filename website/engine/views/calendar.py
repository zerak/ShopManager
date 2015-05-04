#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView

from engine.models import Shop
from engine.forms import EventForm
from fullcalendar.models import CalendarEvent
from fullcalendar.util import events_to_json, calendar_options
from util.custom_view import *
from util.mixins import LoginRequiredMixin

# This is just an example for this demo. You may get this value
# from a separate file or anywhere you want

OPTIONS = """{  timeFormat: "H:mm",
                 buttonText: {
                    today: '今天',
                    month: '月视图',
                    week: '周视图',
                    day: '日视图'
                },
                allDayText: "全天",
                editable: true,
                weekMode: "variable",
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,agendaWeek,agendaDay',
                },
                allDaySlot: false,
                firstDay: 0,
                weekMode: 'liquid',
                slotMinutes: 15,
                 buttonText: {
                    today: '今天',
                    month: '月视图',
                    week: '周视图',
                    day: '日视图'
                },
                defaultEventMinutes: 30,
                minTime: 8,
                maxTime: 20,
                editable: false,
                titleFormat: {
                    month: 'yyyy年 MMMM月',
                    week: "[yyyy年] MMMM月d日 { '&#8212;' [yyyy年] MMMM月d日}",
                    day: 'yyyy年 MMMM月d日 dddd'
                },
                currentTimezone:'Asia/Shanghai',
                monthNames: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                dayNames: ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
                dayClick: function(date, allDay, jsEvent, view) {
                    if (allDay) {
                        $('#calendar').fullCalendar('gotoDate', date)      
                        $('#calendar').fullCalendar('changeView', 'agendaDay')
                    }
                },
                eventClick: function(event, jsEvent, view) {
                    if (view.name == 'month') {
                        $('#calendar').fullCalendar('gotoDate', start)      
                        $('#calendar').fullCalendar('changeView', 'agendaDay')
                    }
                },
            }"""


class EventsView(LoginRequiredMixin, ListSearchView):
    template_name ='shop/calendar.html'
    event_url = 'all_events/'

    def get(self, request):
        form = EventForm()
        return render(request,
                                self.template_name,
                                {'calendar_config_options': calendar_options(self.event_url, OPTIONS),
                                'form':form}
                            )

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            all_day = form.cleaned_data['all_day']
            shop = get_object_or_404(Shop, pk=self.request.session['shop'])
            CalendarEvent.objects.create(title=title,
                                                                start=start,
                                                                end=end,
                                                                all_day=all_day,
                                                                shop=shop
                                                        )
            return HttpResponseRedirect('/engine/shops/calendar')
        else:
            raise form.ValidationError()

def all_events(request):
    events = CalendarEvent.objects.filter(shop_id=request.session['shop'])
    return HttpResponse(events_to_json(events), content_type='application/json')