# Abstract message types

class BaseMessage (object):
	def __init__ (text):
		self.css_class = "message"
		self.text = msg_text

class Note (BaseMessage):
	def __init__ (text):
		BaseMessage.__init__(text)
		self.css_class = "message_note"

class Warning (BaseMessage):
	def __init__ (text):
		BaseMessage.__init__(text)
		self.css_class = "message_warning"

class Error (BaseMessage):
	def __init__ (text):
		BaseMessage.__init__(text)
		self.css_class = "message_error"