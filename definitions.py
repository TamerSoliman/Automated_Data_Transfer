def transfer_and_report():
	"""
		The mastermind. Triggered by CSV creation.
		Checks then prompts file transfer.
		Then prompts email sending .
	"""
	import os, glob
	from definitions import pretransfer_check
	os.chdir("C:/Users/tamer/to_lx")
	files=glob("*.csv")

	if len(files) < 8:
		subj = body = None
	elif len(files) > 8:
		subj= ("Experiment 4: Transfer Problem;"
			"excess files dumped into the windows folder")
		body ="Here are the files {0} {1}".format(
			"\n", "\n".join(files))
	elif not pretransfer_check():
		subj=("Experiment 4: Transfer Problem;"
			" redundent or misnamed files found in the Windows folder")
		body ="Here are the files {0} {1}".format(
			"\n", "\n".join(files))
	else:
		from definitions import send_files
		subj, body = send_files(files)
	send_email(subj, body)

def pretransfer_check(files, prefix=4):
	"""
		Checks if the to-be-transfered file set has no duplicates 				and all belong to the same participant. Returns True or False
	"""
	id="p"+files[0][1 : prefix]
	belong = all([file.startswith(id ) for file in files])
	unique = len(files) == len(set(files))
	return belong & unique


def posttransfer_check(files, after):
	"""
		checks for csv leftovers from previous analysis or current 		file transfer & returns relevant subject line and body of a 			notification 		email
	"""
	lx_leftovers = list(set(after) - set(files))
	win_leftovers = list(set(files) - set(after))
	win_problem = ("Here are the csv's that "
				"failed to transfer{0} {1}").format(
				"\n", "\n".join(win_leftovers))
	lx_problem=("Here are the leftover csv's"
			" from previous analyses{0} {1}").format(
			"\n", "\n".join(lx_leftovers))
	if (len(lx_leftovers)   !=0) & (len(win_leftovers) !=0):
		subj = ("Experiment4: Transfer Problems;"
			" Lx and Win leftovers found!")
		body=win_problem+"\n"+lx_problem
	elif len(lx_leftovers)   !=0:
		subj = "Experiment4: Transfer Problems; Lx  leftovers found!"
		body=lx_problem
	elif len(win_leftovers)   !=0:
		subj = ("Experiment4: Transfer Problems;"
			" CSV's failed to transfer!")
		body=win_problem
	else:
		[os.remove(file) for file in files]
		subj= body = None
	return subj, body


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


