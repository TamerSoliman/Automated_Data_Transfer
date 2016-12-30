1. def transfer_and_report():
2. 	"""
3. 		The mastermind. Triggered by CSV creation.
4. 		Checks then prompts file transfer.
5. 		Then prompts email sending .
6. 	"""
7. 	import os, glob
8. 	from definitions import pretransfer_check
9. 	os.chdir("C:/Users/tamer/to_lx")
10. 	files=glob("*.csv")
11. 
12. 	if len(files) < 8:
13. 		subj = body = None
14. 	elif len(files) > 8:
15. 		subj= ("Experiment 4: Transfer Problem;"
16. 			"excess files dumped into the windows folder")
17. 		body ="Here are the files {0} {1}".format(
18. 			"\n", "\n".join(files))
19. 	elif not pretransfer_check():
20. 		subj=("Experiment 4: Transfer Problem;"
21. 			" redundent or misnamed files found in the Windows folder")
22. 		body ="Here are the files {0} {1}".format(
23. 			"\n", "\n".join(files))
24. 	else:
25. 		from definitions import send_files
26. 		subj, body = send_files(files)
27. 	send_email(subj, body)