from django.shortcuts import get_object_or_404, redirect

from .models import URL


def redirect_to_short_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    url.clicked()

    return redirect(url.full_url)
