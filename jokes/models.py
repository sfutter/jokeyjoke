import datetime
from django.db import models
from django.utils import timezone

class Joke(models.Model):
	joke = models.CharField(max_length=5000)
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.joke


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'