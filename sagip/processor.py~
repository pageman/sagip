from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import date
from django.template import loader, Context, RequestContext
import time
from sagip_main.models import TabInfo, DataBits
from sagip.layers import get_layers_by_name

def process_climate(request):
	if request.user.is_authenticated():
		category = 'climate'
	#optimize me later i am rushing
		if request.POST.get('temp', False):
			print 'temp'
			name='temperature'
			value=float(request.POST['temp'])
			geo_lat=float(request.POST['temp_lat'])
			geo_long=float(request.POST['temp_long'])
			unit = 'C'
			point = DataBits.objects.create(category=category,
										name=name,
										value=value+" "+unit,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('humid', False):
			name='humidity'
			print name
			value=float(request.POST['humid'])
			geo_lat=float(request.POST['humid_lat'])
			geo_long=float(request.POST['humid_long'])
			unit = 'Hg'
			point = DataBits.objects.create(category=category,
										name=name,
										value=value+" "+unit,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('bagyo', False):
			name='rainfall'
			print name
			value=float(request.POST['bagyo'])
			geo_lat=float(request.POST['bagyo_lat'])
			geo_long=float(request.POST['bagyo_long'])
			unit = 'Signal'
			point = DataBits.objects.create(category=category,
										name=name,
										value=value+" "+unit,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('tsun', False):
			name='tsunami'
			
			value=float(request.POST['tsun'])
			geo_lat=float(request.POST['tsun_lat'])
			geo_long=float(request.POST['tsun_long'])
			unit = 'Level'
			
			point = DataBits.objects.create(category=category,
										name=name,
										value=value+" "+unit,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('earth', False):
			name='earthquake',
		
			value=float(request.POST['tsun'])
			geo_lat=float(request.POST['tsun_lat'])
			geo_long=float(request.POST['tsun_long'])
			unit = 'Intensity'
			point = DataBits.objects.create(category=category,
										name=name,
										value=value+" "+unit,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		
		context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'data_names':DataBits.objects.all(),
					}

		return context
	
	else:
		context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'not_user': True,
					
					}
		return context

def process_infra(request):
	if request.user.is_authenticated():
		category = 'infrastructure'
	#optimize me later i am rushing
		if request.POST.get('road_long', False):
			name='road_events'
			unit=request.POST.get('road_block', '')+request.POST.get('road_re', '')+request.POST.get('road_acc', '')+request.POST.get('road_cons', '')
			geo_lat=request.POST['road_lat']
			geo_long=request.POST['road_long']
			value = 1
			point = DataBits.objects.create(category=category,
										name=name,
										value=value,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('rail_long', False):
			name='railway_events'
			unit=request.POST.get('rail_acc', '')+request.POST.get('road_cols', '')+request.POST.get('road_mal', '')
			geo_lat=request.POST['rail_lat']
			geo_long=request.POST['rail_long']
			value = 1
			point = DataBits.objects.create(category=category,
										name=name,
										value=value,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('air_long', False):
			name='airport_events'
			unit=request.POST.get('air_flight', '')+request.POST.get('air_can', '')+request.POST.get('road_acc', '')
			geo_lat=request.POST['air_lat']
			geo_long=request.POST['air_long']
			value = 1
			point = DataBits.objects.create(category=category,
										name=name,
										value=value,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		if request.POST.get('sea_long', False):
			name='seaport_events'
			unit=request.POST.get('sea_block', '')+request.POST.get('sea_re', '')+request.POST.get('sea_mal', '')+request.POST.get('sea_cols', '')
			geo_lat=request.POST['sea_lat']
			geo_long=request.POST['sea_long']
			value = 1
			point = DataBits.objects.create(category=category,
										name=name,
										value=value,
										unit=unit,
										geo_lat=geo_lat,
										geo_long=geo_long,
										contrib_user=request.user)
		context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'data_names':DataBits.objects.all(),
					}

		return context
	
	else:
		context = {
					'date_now':time.strftime('%A, %d %B %Y'),
					'request':request,
					'user':request.user,
					'tabinfos':TabInfo.objects.all(),
					'points': DataBits.objects.all(),
					'not_user': True,
					
					}
		return context

