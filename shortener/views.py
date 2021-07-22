from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView, CreateAPIView
from django.conf import settings
from django.views import View

from  shortener.models import Link
from .serializer import LinkSerializer

# Create your views here.

def handler404(request, *args, **kwargs):
    return render(request, '404.html', status = 404)


def handler500(request, *args, **kwargs):
    return render(request, '500.html', status = 500)


class ShortenerListAPIView(ListAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer 

class ShortenerCreateAPIView(CreateAPIView):
	serializer_class = LinkSerializer 

class Redirector(View):
	def get(self, request, shortened_link, *args, **kwargs):
		shortened_link = settings.HOST_URL + "/" + self.kwargs['shortened_link']
		try:
			redirect_link = Link.objects.filter(shortened_link=shortened_link).first().original_link
		except Exception:
			return render(request, '404.html', status = 404)
		return redirect(redirect_link) 