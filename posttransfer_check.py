1. def posttransfer_check(files, after):
2. 	"""
3. 		checks for csv leftovers from previous analysis or current 		file transfer & returns relevant subject line and body of a 			notification 		email
4. 	"""
5. 	lx_leftovers = list(set(after) - set(files))
6. 	win_leftovers = list(set(files) - set(after))
7. 	win_problem = ("Here are the csv's that "
8. 				"failed to transfer{0} {1}").format(
9. 				"\n", "\n".join(win_leftovers))
10. 	lx_problem=("Here are the leftover csv's"
11. 			" from previous analyses{0} {1}").format(
12. 			"\n", "\n".join(lx_leftovers))
13. 	if (len(lx_leftovers)   !=0) & (len(win_leftovers) !=0):
14. 		subj = ("Experiment4: Transfer Problems;"
15. 			" Lx and Win leftovers found!")
16. 		body=win_problem+"\n"+lx_problem
17. 	elif len(lx_leftovers)   !=0:
18. 		subj = "Experiment4: Transfer Problems; Lx  leftovers found!"
19. 		body=lx_problem
20. 	elif len(win_leftovers)   !=0:
21. 		subj = ("Experiment4: Transfer Problems;"
22. 			" CSV's failed to transfer!")
23. 		body=win_problem
24. 	else:
25. 		[os.remove(file) for file in files]
26. 		subj= body = None
27. 	return subj, body