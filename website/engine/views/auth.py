from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponse, HttpResponseRedirect

from engine.forms import LoginForm, RegisterForm
# Create your views here.

def do_login(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect('/engine/dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_store:
                auth_login(request, user)
                request.session['shop'] = request.user.own_shop.id
            else:
                raise Http404
            return HttpResponseRedirect('/engine/dashboard')
    else:
        form = LoginForm()
    return render(request,
                            'engine/login.html',
                            dict(form=form)
                )

@login_required
def do_logout(request):
    auth_logout(request)
    return render_to_response('engine/index.html')

def do_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/engine/dashboard')
    else:
        form = RegisterForm()
    return render(request,
                            'engine/register.html',
                            dict(form=form),
                )

@login_required
def dashboard(request):
    return render_to_response("shop/dashboard.html",
                                                    dict(user=request.user)
                )