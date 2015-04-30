from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def make_paginator(request, items, per_page=5):
    """Make paginator."""
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    paginator = Paginator(items, per_page)
    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items
