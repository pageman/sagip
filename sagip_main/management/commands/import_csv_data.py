from django.core.management.base import BaseCommand, CommandError

from sagip_main.models import Provinces
import csv


class Command(BaseCommand):
	args = '[csv file]'
	help = 'bulk update of quarter details'
	
	def handle(self, * args, ** options):
		
		reader = csv.reader(open(args[0], 'rb'))
		count = 1
		for row in reader:
			if count is 1:
				count += 1
				continue
			geo_long = row[0]
			geo_lat = row[1]
			name = row[2]
			province = row[3]
			region = row[4]
			area = row[5]
			perimeter = row[6]
			point = Provinces.objects.create(name=name,
										province=province,
										region=region,
										area=area,
										perimeter = perimeter,
										geo_lat=geo_lat,
										geo_long=geo_long)
		print('Script Finished. updated %d database ' % (count))
