1. #!/usr/bin/env python3
2. import time
3. from watchdog.observers import Observer
4. from watchdog.events import PatternMatchingEventHandler
5. 
6. class Watch_and_Trigger(PatternMatchingEventHandler):
7. 	"""
8. 		Daemon-like silent watcher for creation
9. 		of CSV files in specified directory.
10. 		Triggers "transfer-and-report" func.
11. 	"""
12. 	pattern=["*.csv"]
13. 	def  process(self, event):
14. 		from definitions import transfer_and_report
15. 		transfer_and_report()
16. #		print("It Worked!") # uncomment for testing
17. 	def on_created(self, event):
18. 		self.process(event)
19. 
20. if __name__ == '__main__':
21. 	observer = Observer()
22. 	path = "C:/Users/tamer/to_lx"
23. 	observer.schedule(watch_and_trigger(),path)
24. 	observer.start()
25. 
26. 	try:
27. 		while True:
28. 			time.sleep(1)
29. 	except KeyboardInterrupt:
30. 		observer.stop()
31. 	observer.join()