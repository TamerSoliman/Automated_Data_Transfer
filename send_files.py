1. def send_files(files):
2. 	"""
3. 		Transfers files & calls posttransfer_check func
4. 		to varify file transfer.
5. 		Returns two strings to be used as subject line and body
6. 		of notification email
7. 	"""
8. 
9. 	from definitions import posttransfer_check
10. 	import pysftp
11. 	cnopts = pysftp.CnOpts() 
12. 	cnopts.hostkeys = None 
13. 	with pysftp.Connection(host="xxx.x.x.x", port=xxxx, 				username="USERNAME", password="PASSWORD", 
14. 		cnopts=cnopts) as con:
15. 		con.chdir("/home/tamer/from_win")
16. 		[con.put(file) for file in files]
17. 		after =[f for f in con.listdir() if f.endswith("csv")]
18. 		subj, body = posttransfer_check(files, after)
19. 		if subj is None:
20. 			con.execute("touch success.txt")
21. 
22. 	return subj, body