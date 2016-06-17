from django.utils.timezone import now
from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests_oauthlib import OAuth1
from allauth.socialaccount.models import SocialAccount

def index(request):
	return render(request, "mysite/index.html")

def home(request):
    today = datetime.date.today()
    return render(request, "mysite/index.html", {'today': today, 'now': now()})

#def index(request, user):
#	socialaccount = SocialAccount.objects.get(user=request.user, provider="twitter")
#	username = socialaccount.extra_data['first_name']
#	return render_to_response('mysite/index.html',{'username' : username}, context_instance=RequestContext(request))

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")