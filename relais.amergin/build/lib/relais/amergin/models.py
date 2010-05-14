from django.db import models


class Repository (models.Model):
	identifier = models.CharField ('ID',
		max_length=16, primary_key=True,
		help_text="""A unique identifier for the repository.
			This will appear as part of its url.""",
	)
	title = models.CharField ('Title',
		max_length=80,
		help_text="""An informal name for the repository.
			It need not be unique.""",
	)
	description = models.TextField ('Description',
		blank=True,
		help_text="""A short summary of the attached repository.""",
	)
	uri = models.CharField ('URI',
		max_length=96,
		help_text="""The access details for the attached Relais repository""",
	)

	class Meta:
		verbose_name = 'relais repository'
		verbose_name_plural = 'relais repositories'

