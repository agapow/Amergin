
import modelcontroller


class RestController (modelcontroller.ModelController):
	"""
	A model controller provided with a standard set of REST actions.
	
	"""
	
	actions = [
		DefaultAction(),
	]
	
	@classmethod
	def get_title (cls):
		"""
		Find the text that will entitle views.
		"""
		# NOTE: a title is not compulsory, so view should handle the null case
		# TODO: default to capitalised identifier or classname
		return getattr (cls, 'title', "Browsing %s" % cls.get_name_plural())
	






		
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
	

