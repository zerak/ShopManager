from django.shortcuts import render

def stat(request):
    return render(request,
                            'shop/stat.html'
            )