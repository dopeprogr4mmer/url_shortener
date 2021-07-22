from django.db import models
from django.conf import settings
from random import choices
from string import ascii_letters 

# Create your models here.
class Link(models.Model):
	original_link = models.URLField()
	shortened_link = models.URLField(blank=True, null=True)

	def generate_short_link(self):
		while True:
			random_string = ''.join(choices(ascii_letters, k=7))
			new_link = settings.HOST_URL + '/' + random_string 
			if not Link.objects.filter(shortened_link=new_link).exists():
				break 
		return new_link 

	def save(self, *args, **kwargs):
		if not self.shortened_link:
			new_link = self.generate_short_link()
			self.shortened_link = new_link
		return super().save(*args, **kwargs)

