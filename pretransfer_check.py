1. def pretransfer_check(files, prefix=4):
2. 	"""
3. 		Checks if the to-be-transfered file set has no duplicates 				and all belong to the same participant. Returns True or False
4. 	"""
5. 	id="p"+files[0][1 : prefix]
6. 	belong = all([file.startswith(id ) for file in files])
7. 	unique = len(files) == len(set(files))
8. 	return belong & unique
9. 