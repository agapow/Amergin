
from defaultaction import DefaultAction


class BaseController(object):
	"""
	Mapping from urls to views for a related set of actions.
	
	In our scheme, a controller is basically a container of actions, represented
	as a set of urls with the same root. The controller provides the routing to
	specific actions.
	"""
	# TODO: need a way to tell contained actions about controller, e.g. pass name
	# TODO: can we turn all those ugly calls below into class properties?
	
	# identifier = "MUST PROVIDE UNIQUE ID"
	# url = "SHOULD PROVIDE URL"
	# title = "SHOULD PROVIDE READABLE TITLE"
	# description = "SHOULD PROVIDE READABLE DESCRIPTION"
	
	actions = [
		PlaceholderAction ("""There are no actions defined for this class but
			this placeholder, you should really define one."""),
	]

	@classmethod
	def get_identifier (cls):
		"""
		Find the unique identifier for this controller.
		
		Currently, this is largely used for other controller properties (e.g.
		the name and url) but may in the future be used for distinguishing
		different controllers.
		"""
		return getattr (cls, 'identifier', cls.__name__.lower())

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
		return getattr (cls, 'title', '')
		
	@classmethod
	def get_description (cls):
		"""
		Find the descriptor that appear on views.
		"""
		# NOTE: a description is not compulsory, so view should handle the null case
		return getattr (cls, 'title', '')
	
	@classmethod
	def get_views (cls):
		"""
		Return a list of the urls and actions contained in this controller.
		"""
		return [(x.url, x) for x in cls.actions]

	






		
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
	

