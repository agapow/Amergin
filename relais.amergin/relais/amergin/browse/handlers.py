

from piston.handler import BaseHandler
from relais.amergin import models

class BioseqHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = models.Bioseq   

   def read(self, request, post_slug):
      ...