import logging

def setup_logger():
	# set up logging to file
	logging.basicConfig(
	     filename='log.txt',
	     level=logging.DEBUG, 
	     format= '%(asctime)s - %(message)s',
	     datefmt='%H:%M:%S'
	 )

	# set up logging to console
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	# set a format which is simpler for console use
	formatter = logging.Formatter('%(asctime)s - %(message)s', "%Y-%m-%d %H:%M:%S")
	console.setFormatter(formatter)
	# add the handler to the root logger
	logging.getLogger('').addHandler(console)

