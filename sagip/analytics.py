from sagip_main.models import TabInfo, DataBits, Provinces
from scipy import stats,array
from django.db.models import Avg, Max, Min

def get_stats(data):
	stats={}
	mean_val = 0
	if data is 'temp':
		stats['temp_mean'] = DataBits.objects.filter(name='temperature').aggregate(Avg('value'))
		stats['temp_max'] = DataBits.objects.filter(name='temperature').aggregate(Max('value'))
		stats['temp_min'] = DataBits.objects.filter(name='temperature').aggregate(Min('value'))
#		stats['temp_var'] = DataBits.objects.filter(name='temperature').aggregate(StdDev('value'))
	elif data is 'humid':
		stats['humid_mean'] = DataBits.objects.filter(name='humidity').aggregate(Avg('value'))
		stats['humid_max'] = DataBits.objects.filter(name='humidity').aggregate(Max('value'))
		stats['humid_min'] = DataBits.objects.filter(name='humidity').aggregate(Min('value'))
#		stats['humid_var'] = DataBits.objects.filter(name='humidity').aggregate(StdDev('value'))
		
	elif data is 'rain':
		stats['rain_mean'] = DataBits.objects.filter(name='rain').aggregate(Avg('value'))
		stats['rain_max'] = DataBits.objects.filter(name='rain').aggregate(Max('value'))
		stats['rain_min'] = DataBits.objects.filter(name='rain').aggregate(Min('value'))
#		stats['rain_var'] = DataBits.objects.filter(name='rain').aggregate(StdDev('value'))

	else:
		stats['mean'] = 0
		stats['max'] = 0
		stats['min'] = 0
		stats['var'] = 0
	
	return stats

def mean(nums):
	if len(nums):
		return float( sum(nums) / len(nums))
	else:
		return 0.0

def min_value(nums):
	if len(nums):
		return float( sum(nums) / len(nums))
	else:
		return 0.0
	
