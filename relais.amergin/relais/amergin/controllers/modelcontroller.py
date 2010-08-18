
import basecontroller


class ModelController (basecontroller.BaseController):
	"""
	A controller based on a model.
	
	Mainly uses the model to provide names and so forth.
	"""
	
	model = None
	# name = "CAN PROVIDE READABLE NAME"
	# name_plural = "CAN PROVIDE READABLE NAME FOR PLURALS"
	
	actions = [
		DefaultAction(),
	]
	
	@classmethod
	def get_name (cls):
		return getattr (cls, 'name', cls.model._meta.verbose_name)
		
	@classmethod
	def get_name_plural (cls):
		return getattr (cls, 'name_plural', cls.model._meta.verbose_name_plural)

	@classmethod
	def get_identifier (cls):
		"""
		Find the unique identifier for this controller.
		
		Currently, this is largely used for other controller properties (e.g.
		the name and url) but may in the future be used for distinguishing
		different controllers.
		"""
		return getattr (cls, 'identifier', cls.get_name_plural())

	@classmethod
	def get_url (cls):
		"""
		Find the url component that directs towards this controller.
		"""
		return getattr (cls, 'url', cls.get_identifier())
	
	@classmethod
	def get_title (cls):
		"""
		Find the text that will entitle views.
		"""
		# NOTE: a title is not compulsory, so view should handle the null case
		# TODO: default to capitalised identifier or classname
		return getattr (cls, 'title', cls.get_name_plural())
	






		
	@classmethod
	def url (cls):
		return "%s/browse/%s" % (settings.AMERGIN_URL, cls.identifier)
		
	@classmethod
	def index_url (cls):
		return cls.url()

	@classmethod
	def create_url (cls):
		return "%s/create" % cls.index_url()
		
	@classmethod
	def destroy_url (cls, id):
		return "%s/%s/destroy" % (cls.index_url(), id)
		
	@classmethod
	def edit_url (cls, id):
		return "%s/%s/edit" % (cls.index_url(), id)
		
	@classmethod
	def view_url (cls, id):
		return "%s/%s/edit" % (cls.index_url(), id)
		
	@classmethod
	def index (cls, request):
		found_objs = cls.model.objects.all()
		return render_to_response('relais.amergin/base_browse_index.html', {
				'name' : cls.model._meta.verbose_name,
				'plural_name' : cls.model._meta.verbose_name_plural,
				'objects': found_objs,
				'obj_cnt': len (found_objs),
			}
		)
	
	@classmethod
	def view (cls, id=None):
		found_objs = cls.model.objects.all()
		try: 
			obj = cls.model.objects.get(identifier=id)
		except cls.model.DoesNotExist:
			# we have no object!  do something
			obj = None
		return render_to_response('relais.amergin/base_browse_view.html', {
				'name' : cls.model._meta.verbose_name,
				'plural_name' : cls.model._meta.verbose_name_plural,
				'object': obj,
			}
		)
		
	@classmethod
	def create (cls):
		return HttpResponse("Hello world")
	
	@classmethod
	def destroy (cls, id):
		return HttpResponse("Hello world")
	
	@classmethod
	def edit (cls, id):
		return HttpResponse("Hello world")
	

