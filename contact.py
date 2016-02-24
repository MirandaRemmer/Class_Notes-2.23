#activity 1

class Contact(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile = ""
		self.work_number = ""
		self.email = ""
		self.birthday = ""
		self.company = ""
		self.notes = ""
	def send_email(self, message):
		print "To: %s - \n\t%s:\n\t\t%s" % (self.email, self.first_name, message)


