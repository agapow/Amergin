from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponsePermanentRedirect

import relais.amergin.urls

from django.conf import settings

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^amergin/', include(relais.amergin.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
	# redir front page to amergin
	(r'^$', lambda request: HttpResponsePermanentRedirect('/amergin')),
)
