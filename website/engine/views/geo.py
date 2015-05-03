from django.shortcuts import render

def geo(request):
    return render(request,
                            'shop/geo.html',
                )