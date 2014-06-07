from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import date
from django.template import loader, Context, RequestContext
import time
from sagip_main.models import TabInfo, DataBits
from sagip.layers import get_layers_by_name
from sagip.processor import *

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
