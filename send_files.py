def send_files(files):
	"""
		Transfers files & calls posttransfer_check func
		to varify file transfer.
		Returns two strings to be used as subject line and body
		of notification email
	"""

	from definitions import posttransfer_check
	import pysftp
	cnopts = pysftp.CnOpts() 
	cnopts.hostkeys = None 
	with pysftp.Connection(host="xxx.x.x.x", port=xxxx, 				username="USERNAME", password="PASSWORD", 
		cnopts=cnopts) as con:
		con.chdir("/home/tamer/from_win")
		[con.put(file) for file in files]
		after =[f for f in con.listdir() if f.endswith("csv")]
		subj, body = posttransfer_check(files, after)
		if subj is None:
			con.execute("touch success.txt")

	return subj, body