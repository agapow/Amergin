# Abstract message types

class BaseMessage (object):
	def __init__ (self, text, css_class="info"):
		self.css_class = css_class
		self.text = text

class Note (BaseMessage):
	def __init__ (self, text):
		BaseMessage.__init__(self, text, "info")


Info = Note
Success = Note

class Warning (BaseMessage):
	def __init__ (self, text):
		BaseMessage.__init__(self, text, "warning")


class Error (BaseMessage):
	def __init__ (self, text):
		BaseMessage.__init__(self, text, "error")
