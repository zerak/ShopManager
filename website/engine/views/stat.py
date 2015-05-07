from django.shortcuts import render

def stat(request):
    return render(request,
                            'shop/stat.html'
                )

def data(request):
    return render(request,
                            'shop/data.html'
                )