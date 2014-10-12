from django.contrib import admin
from jokes.models import Joke
import datetime


class JokeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['joke']}),
		('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),	
	]

	list_display = ('joke', 'likes','pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['joke']


admin.site.register(Joke, JokeAdmin)
