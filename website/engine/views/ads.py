from django.shortcuts import render, get_object_or_404

from util.mixins import LoginRequiredMixin
from util.custom_view import *

def index(request):
    return render(request,
                            'shop/ads.html')

class AdsView(LoginRequiredMixin, ListRelated):
    template_name = 'shop/ads.html'