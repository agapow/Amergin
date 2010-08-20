from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponsePermanentRedirect

import relais.amergin.urls

from django.conf import settings

urlpatterns = patterns ('',
	# capture admin requests
	(r'^admin/', include(admin.site.urls)),
	# place amergin app at '/amergin' and redir head of site to there
	(r'^amergin/', include(relais.amergin.urls)),
	# redir front page to amergin
	(r'^$', lambda request: HttpResponsePermanentRedirect('/amergin')),
	# serve media
	# TODO: is this necessary?
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
)
