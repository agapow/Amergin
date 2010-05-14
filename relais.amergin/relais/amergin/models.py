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


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

#class AmerginRepository(models.Model):
#    identifier = models.CharField(max_length=16, primary_key=True)
#    title = models.CharField(max_length=80)
#    description = models.TextField()
#    uri = models.CharField(max_length=96)
#    class Meta:
#        db_table = u'amergin_repository'

class Assay (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = models.CharField(max_length=72, blank=True)
	description = models.TextField(blank=True)
	source = models.CharField(max_length=32, blank=True)
	type = models.CharField(max_length=32, blank=True)
	format = models.CharField(max_length=32, blank=True)
	results = models.TextField(blank=True)
	sample_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'assays'

class Bioseqannotation (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	name = models.CharField(max_length=32, blank=True)
	value = models.TextField(blank=True)
	biosequence_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqannotations'

class Bioseqcollection (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = models.CharField(max_length=72, blank=True)
	description = models.TextField(blank=True)
	source = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqcollections'

class BioseqcollectionsBioseq (models.Model):
	collection_id = models.CharField(max_length=32, primary_key=True)
	biosequence_id = models.CharField(max_length=32, primary_key=True)
	class Meta:
	    db_table = u'bioseqcollections_biosequences'

class Bioseqextref (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	urn = models.CharField(max_length=72, blank=True)
	biosequence_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqextrefs'

class Bioseqfeature (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	location = models.CharField(max_length=32, blank=True)
	type = models.CharField(max_length=32, blank=True)
	biosequence_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqfeatures'

class Bioseqqualifier (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	name = models.CharField(max_length=32, blank=True)
	value = models.TextField(blank=True)
	seqfeature_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'bioseqqualifiers'

class Bioseq (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = models.CharField(max_length=72, blank=True)
	description = models.TextField(blank=True)
	source = models.CharField(max_length=32, blank=True)
	seqtype = models.CharField(max_length=32, blank=True)
	seqdata = models.TextField(blank=True)
	sample_id = models.CharField(max_length=32, blank=True)
	class Meta:
		db_table = u'biosequences'
		verbose_name = 'biosequence'
		verbose_name_plural = 'biosequences'
		
class Document (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = models.CharField(max_length=72, blank=True)
	description = models.TextField(blank=True)
	source = models.CharField(max_length=32, blank=True)
	filename = models.CharField(max_length=72, blank=True)
	fileformat = models.CharField(max_length=32, blank=True)
	content = models.TextField(blank=True) # This field type is a guess.
	sample_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'documents'

class Region (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = models.CharField(max_length=72, blank=True)
	description = models.TextField(blank=True)
	synonyms = models.TextField(blank=True)
	centroid_lat = models.TextField(blank=True) # This field type is a guess.
	centroid_lon = models.TextField(blank=True) # This field type is a guess.
	type = models.CharField(max_length=32, blank=True)
	within_region_id = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'regions'

class Sample (models.Model):
	identifier = models.CharField(max_length=32, primary_key=True)
	title = models.CharField(max_length=72, blank=True)
	description = models.TextField(blank=True)
	source = models.CharField(max_length=32, blank=True)
	locn_lat = models.TextField(blank=True) # This field type is a guess.
	locn_lon = models.TextField(blank=True) # This field type is a guess.
	locn_method = models.CharField(max_length=32, blank=True)
	address = models.TextField(blank=True)
	country = models.CharField(max_length=72, blank=True)
	region_id = models.CharField(max_length=32, blank=True)
	date_collected = models.DateTimeField(null=True, blank=True)
	date_collected_exact = models.NullBooleanField(null=True, blank=True)
	date_received = models.DateTimeField(null=True, blank=True)
	final_result = models.CharField(max_length=32, blank=True)
	host = models.CharField(max_length=32, blank=True)
	status = models.CharField(max_length=32, blank=True)
	class Meta:
	    db_table = u'samples'
