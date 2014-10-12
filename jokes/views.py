from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from jokes.models import Joke

def index(request):
	latest_joke_list = Joke.objects.order_by('-pub_date')[:5]
	context = {'latest_joke_list': latest_joke_list}
    	return render(request, 'jokes/index.html', context)

#OLD CODE FOR DEMONSTRATION OF HOW VIEWS WORK
#this code would be fine, but to keep the views file simple
#we move the code into a template. See templates/index.html for 
#this method's view
#	latest_joke_list = Joke.objects.order_by('-pub_date')[:5]
#	output = ', '.join([p.joke for p in latest_joke_list])
#	return HttpResponse(output)

def detail(request, joke_id):
	joke = get_object_or_404(Joke, pk=joke_id)
	return render(request,'jokes/detail.html', {'joke':joke}) 

def results(request, joke_id):
    return HttpResponse("You're looking at the results of joke %s." % joke_id)

def like(request, joke_id):
	j = Joke.objects.get(pk=joke_id)
	count = j.likes
	count += 1
	j.likes = count
	j.save()

	latest_joke_list = Joke.objects.order_by('-pub_date')[:5]
	context = {'latest_joke_list': latest_joke_list}
    	return render(request, 'jokes/index.html', context)
	# return HttpResponse("Thank you. + 1 like for joke %s." % joke_id)

