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