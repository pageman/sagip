from django.conf.urls import patterns, include, url

from django.contrib import admin
import app.urls
from sagip_main import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sagip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'sagip.views.home', name='home'),
	url(r'^data/', 'sagip.views.data', name='contrib_data'),
	url(r'^view_map/', 'sagip.views.view_map', name='view_map'),
	url(r'^analytics/', 'sagip.views.analytics', name='analytics'),
	url(r'^climate/', 'sagip.views.climate', name='climate'),
	url(r'^infra/', 'sagip.views.infra', name='infra'),
	url(r'^disaster/', 'sagip.views.disaster', name='disaster'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
#    url(r'^data/', include(sagip_main.urls)),
#    url(r'^data/', 'sagip_main.views.contrib_data', name='contrib_data'),
#      url(r'', include('social_auth.urls')),
)
