def pretransfer_check(files, prefix=4):
	"""
		Checks if the to-be-transfered file set has no duplicates 				and all belong to the same participant. Returns True or False
	"""
	id="p"+files[0][1 : prefix]
	belong = all([file.startswith(id ) for file in files])
	unique = len(files) == len(set(files))
	return belong & unique
