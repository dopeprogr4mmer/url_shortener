from django.urls import path
from .views import ShortenerListAPIView, ShortenerCreateAPIView

app_name = 'shortener'

urlpatterns = [
	path('all-links/', ShortenerListAPIView.as_view(), name='all-links'),
	path('', ShortenerCreateAPIView.as_view(), name='create-link'),	
]
