
from relais.amergin import models
from registry import register_controller

class BioseqController(BaseController):
	model = models.Bioseq
	identifier = "bioseqs"
	title = "Biosequences"
	description = "Molecular sequences derived from isolates."
	
register_controller(BioseqController)