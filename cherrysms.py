from httplib import HTTPConnection
import httplib
import urllib
import md5

class SMSException(Exception):
	pass

class SMSSender:
	SMS_HOST = 'gw.cherry-sms.com'
	SEND_BASE = "/index.php?"

	http = None

	def __init__(self, username, password):
		self.username = username
		self.password = md5.new(password).hexdigest()

	def get_http(self):
		if self.http == None:
			self.http = HTTPConnection(self.SMS_HOST)

		return self.http

	def send_sms(self, to, msg):
		http = self.get_http()

		qstr = urllib.urlencode({
			'user': self.username,
			'password': self.password,
			'to': to,
			'message': msg,
			'from': '0'
		})
		url = self.SEND_BASE + qstr
		#print url
			
		http.request("GET", url)
		resp = http.getresponse()

		if resp.status != httplib.OK:
			raise SMSException("Non-200 error code")

		data = resp.read().split("\n")
		#print "error: %s, count: %s, remaining: %s" % (data[0], data[1], data[2])

		if data[0] != "100":
			raise SMSException("Sending failed: " + data[0])
