from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponsePermanentRedirect

import relais.amergin.urls

from django.conf import settings


urlpatterns = patterns ('',
	# capture admin requests at /admin & /admin/...
	(r'^admin/', include(admin.site.urls)),
	('^admin$', lambda request: HttpResponsePermanentRedirect (r'/admin/')),
	# capture amergin requests at site root, /amergin and /amergin/...
	(r'^$', lambda request: HttpResponsePermanentRedirect(r'/amergin/')),
	(r'^amergin/', include(relais.amergin.urls)),
	('^amergin$', lambda request: HttpResponsePermanentRedirect (r'/amergin/')),
	
	# serve media
	# NOTE: works
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
)
