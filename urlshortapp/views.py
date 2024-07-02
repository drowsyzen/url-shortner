from django.shortcuts import redirect
from urlshortapp.models import URLModel
# Example map of shortened to longer URLs

def generate_short_url(request):
    pass

def catch_all(request):
    original_url = request.path
    redirect_url = URLModel.objects.filter(original_url=original_url).first().redirect_url

    print(redirect_url)

    if redirect_url:
        return redirect(redirect_url)
    else:
        return redirect('/default-path')  # Redirect to a default path if not found
