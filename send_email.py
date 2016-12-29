def send_email(subj, body):
	"""
		Receives 2 string args & sends them
		as subject line and body of an email alert
	"""

	if subj is not None:
		import yagmail
		with yagmail.SMTP("USERNAME@gmail.com",
			"PASSWORD") as yag:
			yag.send(to="USERNAME@HOST.com", 
				subject = subj, contents = body)