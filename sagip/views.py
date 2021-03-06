from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import date
from django.template import loader, Context, RequestContext
import time
from sagip_main.models import TabInfo, DataBits, Contact
from sagip.layers import get_layers_by_name
from sagip.processor import *
from sagip.analytics import *
import urllib
import urllib2
import random

# Create your views here.
def home(request):
	
	context = {
				'date_now':time.strftime('%A, %d %B %Y'),
				'request':request,
				'user':request.user,
				'tabinfos':TabInfo.objects.all(),
				'points': DataBits.objects.all(),
				}
#	return render(request, 'sagip_main/index.html', context)
	return render_to_response('sagip_main/index.html', context, RequestContext(request))
	
def view_map(request):
	layers, layer_names = get_layers_by_name()
	context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'layers': layers,
					'layer_names': layer_names,
					}
#	return render(request, 'sagip_main/index.html', context)
	return render_to_response('sagip_main/view_map.html', context, RequestContext(request))
	
def data(request):
	if request.user.is_authenticated():
		if (request.POST['name'] is 'temperature'):
			category = 'climate'
			unit = 'C'
		elif (request.POST['name'] is 'humidity'):
			category = 'climate'
			unit = 'RH'
		elif (request.POST['name'] is 'rainfall'):
			category = 'climate'
			unit = 'MM'
		elif (request.POST['name'] is 'carbon'):
			category = 'climate'
			unit = 'Gg'
		else : 
			category =''
			unit=''
		point = DataBits.objects.create(category=category,
										name=request.POST['name'],
										value=request.POST['value'],
										unit=unit,
										geo_lat=request.POST['geo_lat'],
										geo_long=request.POST['geo_long'],
										contrib_user=request.user)
		context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'data_names':DataBits.objects.all(),
					}
	#	return render(request, 'sagip_main/index.html', context)
		return render_to_response('sagip_main/view_map.html', context, RequestContext(request))
	
	else:
		context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'not_user': True,
					
					}
		return render_to_response('sagip_main/index.html', context,
                                  RequestContext(request))

# Create your views here.
def analytics(request):
	layers, layer_names = get_layers_by_name()
	context = {
				'date_now':time.strftime('%A, %d %B %Y'),
				'request':request,
				'user':request.user,
				'tabinfos':TabInfo.objects.all(),
				'points': DataBits.objects.all(),
				'layers': layers,
				'layer_names': layer_names,
				}
#	return render(request, 'sagip_main/index.html', context)
	return render_to_response('sagip_main/analytics.html', context, RequestContext(request))

def climate(request):
	
	context = process_climate(request)
	layers, layer_names = get_layers_by_name()
	context['layers']=layers
	context['layer_names']=layer_names
	context['govts']=Contact.objects.all()
	
	
	context['temp_mean'] = get_stats('temp')['temp_mean']['value__avg'] 
#	context['temp_var'] = get_stats('temp')['temp_var']
	context['temp_min'] = get_stats('temp')['temp_min']['value__min']
	context['temp_max'] = get_stats('temp')['temp_max']['value__max']
	context['humid_mean'] = get_stats('humid')['humid_mean']['value__avg'] 
#	context['humid_var'] = get_stats('humid')['humid_var']
	context['humid_min'] = get_stats('humid')['humid_min']['value__min']
	context['humid_max'] = get_stats('humid')['humid_max']['value__max']
	context['rain_mean'] = get_stats('rain')['rain_mean']['value__avg'] 
#	context['rain_var'] = get_stats('rain')['rain_var']
	context['rain_min'] = get_stats('rain')['rain_min']['value__min']
	context['rain_max'] = get_stats('rain')['rain_max']['value__max']
	
	
	return render_to_response('sagip_main/climate.html', context, RequestContext(request))
	
def infra(request):
	context = process_infra(request)
	layers, layer_names = get_layers_by_name()
	context['layers']=layers
	context['layer_names']=layer_names
	
	return render_to_response('sagip_main/infra.html', context, RequestContext(request))

def disaster(request):
	layers, layer_names = get_layers_by_name()
	context = {
				'date_now':time.strftime('%A, %d %B %Y'),
				'request':request,
				'user':request.user,
				'tabinfos':TabInfo.objects.all(),
				'points': DataBits.objects.all(),
				'layers': layers,
				'layer_names': layer_names,
				}
#	return render(request, 'sagip_main/index.html', context)
	return render_to_response('sagip_main/disaster.html', context, RequestContext(request))

def turismo(request):
	layers, layer_names = get_layers_by_name()
	context = {
				'date_now':time.strftime('%A, %d %B %Y'),
				'request':request,
				'user':request.user,
				'tabinfos':TabInfo.objects.all(),
				'points': DataBits.objects.all(),
				'layers': layers,
				'layer_names': layer_names,
				}
#	return render(request, 'sagip_main/index.html', context)
	return render_to_response('sagip_main/turismo.html', context, RequestContext(request))

def game(request, page_id):
	layers, layer_names = get_layers_by_name()
	context = {
				'date_now':time.strftime('%A, %d %B %Y'),
				'request':request,
				'user':request.user,
				'tabinfos':TabInfo.objects.all(),
				'points': DataBits.objects.all(),
				'layers': layers,
				'layer_names': layer_names,
				}
#	return render(request, 'sagip_main/index.html', context)
	return render_to_response('sagip_main/15.html', context, RequestContext(request))
	
def send_sms(request):
	if request.user.is_authenticated():
		msg = request.POST['msg']
		num = request.POST['num']
		
		post_data = [('message_type','SEND'),
					('mobile_number','639055541112'),
					('shortcode','29290718255'),
					('message_id','kgkjgbkgsdlh'),
					('message',str(msg)),
					('client_id','a4382ae2034d604f2539dc0f60e1a0425cac96ea59c1a9bc3e7139ba28019277'),
					('secret_key','5661810d0cd4bb8dee44b9dfce5e63b92680ed599485e547ca0117162b316aab'),
					]     # a sequence of two element tuples
		result = urllib2.urlopen('http://post.chikka.com/smsapi/request', urllib.urlencode(post_data))
		content = result.read()
		return render_to_response('sagip_main/reply.html', {'chikka_reply':content,}, RequestContext(request))
	else:
		return render_to_response('sagip_main/not_authorized.html', {'reply':'reply'}, RequestContext(request))	
#	return render(request, 'sagip_main/index.html', context)


def send_alarm(request):
	if request.user.is_authenticated():
	
		msg_id = random.random()
		post_data = [('message_type','SEND'),
					('mobile_number','639055541112'),
					('shortcode','29290718255'),
					('message_id','1234325dfggjd'),
					('message','Alarm triggered by web app'),
					('client_id','a4382ae2034d604f2539dc0f60e1a0425cac96ea59c1a9bc3e7139ba28019277'),
					('secret_key','5661810d0cd4bb8dee44b9dfce5e63b92680ed599485e547ca0117162b316aab'),
					]     # a sequence of two element tuples
		result = urllib2.urlopen('http://post.chikka.com/smsapi/request', urllib.urlencode(post_data))
		content = result.read()
		return render_to_response('sagip_main/reply.html', {'chikka_reply':content,}, RequestContext(request))
	else:
		return render_to_response('sagip_main/not_authorized.html', {'reply':'reply'}, RequestContext(request))	
#	return render(request, 'sagip_main/index.h
