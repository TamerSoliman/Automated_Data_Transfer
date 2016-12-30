1. def send_email(subj, body):
2. 	"""
3. 		Receives 2 string args & sends them
4. 		as subject line and body of an email alert
5. 	"""
6. 
7. 	if subj is not None:
8. 		import yagmail
9. 		with yagmail.SMTP("USERNAME@gmail.com",
10. 			"PASSWORD") as yag:
11. 			yag.send(to="USERNAME@HOST.com", 
12. 				subject = subj, contents = body)