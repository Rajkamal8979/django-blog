from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse

class post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	title = models.CharField(max_length=200)
	text = models.TextField()
	image=models.FileField(null=True,blank=True)
	date_created= models.DateTimeField(auto_now=False,auto_now_add=True)
	date_edited= models.DateTimeField(auto_now=True,auto_now_add=False)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return  reverse('postdetail',{'id':self.id})

# Create your models here.
