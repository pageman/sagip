from django.contrib import admin
from sagip_main.models import Disaster, TabInfo, DataBits, Provinces, Contact
# Register your models here.

class DisasterAdmin(admin.ModelAdmin):
	model = Disaster()

class TabInfoAdmin(admin.ModelAdmin):
	model = TabInfo()
	
class DataBitsAdmin(admin.ModelAdmin):
	model = TabInfo()

class ProvincesAdmin(admin.ModelAdmin):
	model = Provinces()

class ContactAdmin(admin.ModelAdmin):
	model = Provinces()
	
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(TabInfo, TabInfoAdmin)
admin.site.register(DataBits, DataBitsAdmin)
admin.site.register(Provinces, ProvincesAdmin)
admin.site.register(Contact, ContactAdmin)
