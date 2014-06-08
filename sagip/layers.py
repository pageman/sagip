from django.utils.safestring import mark_safe
from sagip_main.models import TabInfo, DataBits


def get_layers_by_name():
	layers =''
	layer =''
	layer_names_holder = DataBits.objects.filter().values("name").distinct()
	layer_names=[]
	for layer_name in layer_names_holder:
		layer_names.append(str(layer_name['name']))
	
	
	for name in layer_names:
		layer = "var "+str(name)+" = L.layerGroup([" 
		points = DataBits.objects.filter(name=str(name))
		
		for point in points:
			temp_point=''
			icon = ''
			if point.name == "temperature": 
				icon = "tempMarker"
			elif point.name == "humidity": 
				icon = "humidMarker"
			elif point.name == "carbon": 
				icon = "carbonMarker"
			else: 
				icon = "rainMarker"
			
			if point.category is 'climate':
				temp_point = "L.marker(["+str(point.geo_lat)+","+str(point.geo_long)+"],{icon:"+icon+"}).bindLabel('"+str(point.value)+"', { noHide: true })"
			else:
				temp_point = "L.marker(["+str(point.geo_lat)+","+str(point.geo_long)+"],{icon:"+icon+"}).bindLabel('"+str(point.unit)+"', { noHide: true })"
			layer += temp_point+","

		layer += "]).addTo(map);"
		layers += layer

	return mark_safe(layers), layer_names
	
#def get_layers_by_category(self):
#	layers={
#	
#	}
#	return 
