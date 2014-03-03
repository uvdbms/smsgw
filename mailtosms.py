import email

class MailToSmsException(Exception):
	pass

class MailToSms(object):
	smsgw = None
	phoneno = None

	def __init__(self, smsgw, phoneno):
		self.smsgw = smsgw
		self.phoneno = phoneno

	def parse_msg_from_str(self, msg_str):
		msg = email.message_from_str(msg_str)
		self.parse_msg(msg)

	def parse_msg_from_file(self, msg_fh):
		msg = email.message_from_file(msg_fh)
		self.parse_msg(msg)

	def parse_msg(self, msg):
		txt = None
		if msg.is_multipart():
			for part in msg.walk():
				if part.get_content_maintype() == "text":
					txt = part.get_payload()
		elif msg.get_content_maintype() == "text":
			txt = msg.get_payload()

		if txt == None:
			raise MailToSmsException()

		sms_text = "[" + msg["Subject"] + "] " + txt

		self.smsgw.send_sms(self.phoneno, sms_text)

