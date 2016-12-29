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