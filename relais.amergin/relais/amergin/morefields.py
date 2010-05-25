from django.db import models
from django import forms

class BetterTextField (models.TextField):

	def __init__(self, *args, **kwargs):
		self.widget_attrs =  {'widget': forms.Textarea}
		if kwargs.has_key('widget_attrs'):
			self.widget_attrs = kwargs['widget_attrs']
			del kwargs['widget_attrs']
		super (BetterTextField, self).__init__(*args, **kwargs)

	def formfield(self, **kwargs):
		kwargs.update (self.widget_attrs)
		return super (BetterTextField, self).formfield (form_class=kwargs)
