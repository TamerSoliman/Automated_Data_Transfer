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
28. 
29. def pretransfer_check(files, prefix=4):
30. 	"""
31. 		Checks if the to-be-transfered file set has no duplicates 				and all belong to the same participant. Returns True or False
32. 	"""
33. 	id="p"+files[0][1 : prefix]
34. 	belong = all([file.startswith(id ) for file in files])
35. 	unique = len(files) == len(set(files))
36. 	return belong & unique
37. 
38. 
39. def posttransfer_check(files, after):
40. 	"""
41. 		checks for csv leftovers from previous analysis or current 		file transfer & returns relevant subject line and body of a 			notification 		email
42. 	"""
43. 	lx_leftovers = list(set(after) - set(files))
44. 	win_leftovers = list(set(files) - set(after))
45. 	win_problem = ("Here are the csv's that "
46. 				"failed to transfer{0} {1}").format(
47. 				"\n", "\n".join(win_leftovers))
48. 	lx_problem=("Here are the leftover csv's"
49. 			" from previous analyses{0} {1}").format(
50. 			"\n", "\n".join(lx_leftovers))
51. 	if (len(lx_leftovers)   !=0) & (len(win_leftovers) !=0):
52. 		subj = ("Experiment4: Transfer Problems;"
53. 			" Lx and Win leftovers found!")
54. 		body=win_problem+"\n"+lx_problem
55. 	elif len(lx_leftovers)   !=0:
56. 		subj = "Experiment4: Transfer Problems; Lx  leftovers found!"
57. 		body=lx_problem
58. 	elif len(win_leftovers)   !=0:
59. 		subj = ("Experiment4: Transfer Problems;"
60. 			" CSV's failed to transfer!")
61. 		body=win_problem
62. 	else:
63. 		[os.remove(file) for file in files]
64. 		subj= body = None
65. 	return subj, body
66. 
67. 
68. def send_email(subj, body):
69. 	"""
70. 		Receives 2 string args & sends them
71. 		as subject line and body of an email alert
72. 	"""
73. 
74. 	if subj is not None:
75. 		import yagmail
76. 		with yagmail.SMTP("USERNAME@gmail.com",
77. 			"PASSWORD") as yag:
78. 			yag.send(to="USERNAME@HOST.com", 
79. 				subject = subj, contents = body)
80. 
81. 
82. def send_files(files):
83. 	"""
84. 		Transfers files & calls posttransfer_check func
85. 		to varify file transfer.
86. 		Returns two strings to be used as subject line and body
87. 		of notification email
88. 	"""
89. 
90. 	from definitions import posttransfer_check
91. 	import pysftp
92. 	cnopts = pysftp.CnOpts() 
93. 	cnopts.hostkeys = None 
94. 	with pysftp.Connection(host="xxx.x.x.x", port=xxxx, 				username="USERNAME", password="PASSWORD", 
95. 		cnopts=cnopts) as con:
96. 		con.chdir("/home/tamer/from_win")
97. 		[con.put(file) for file in files]
98. 		after =[f for f in con.listdir() if f.endswith("csv")]
99. 		subj, body = posttransfer_check(files, after)
100. 		if subj is None:
101. 			con.execute("touch success.txt")
102. 
103. 	return subj, body
104. 
105. 
106. 