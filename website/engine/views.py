from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


from forms import LoginForm, RegisterForm
# Create your views here.

def do_login(request):
    if request.user.is_authenticated():
            return HttpResponseRedirect('/engine/dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return render(request,
                                    'engine/dashboard.html',
                                    dict(user=request.user)
            )
    else:
        form = LoginForm()
    return render(request,
                            'engine/login.html',
                            dict(form=form)
    )

@login_required(login_url='do_login')
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

@login_required(login_url='do_login')
def dashboard(request):
    return render_to_response("engine/dashboard.html")