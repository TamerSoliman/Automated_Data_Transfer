#!/usr/bin/env python3
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Watch_and_Trigger(PatternMatchingEventHandler):
	"""
		Daemon-like silent watcher for creation
		of CSV files in specified directory.
		Triggers "transfer-and-report" func.
	"""
	pattern=["*.csv"]
	def  process(self, event):
		from definitions import transfer_and_report
		transfer_and_report()
#		print("It Worked!") # uncomment for testing
	def on_created(self, event):
		self.process(event)

if __name__ == '__main__':
	observer = Observer()
	path = "C:/Users/tamer/to_lx"
	observer.schedule(watch_and_trigger(),path)
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()