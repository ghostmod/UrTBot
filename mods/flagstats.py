import time
api = None

_name = "Flag Stats"
_author = "B1naryth1ef"
_version = 0.1



class Timer(object):
	def __init__(self):
		self.startt = 0
		self.endt = 0
		self.status = 0
	
	def start(self): 
		if self.status == 0:
			self.startt = time.time()
			self.status = 1
	def stop(self):
		if self.status == 1: 
			self.endt = time.time()
			self.status = 0
	def value(self): return self.endt-self.startt
	def reset(self):
		self.start = 0
		self.end = 0
		self.status = 0

redFlag = Timer()
blueFlag = Timer()

def eventListener(obj):
	global api
	if obj == 'init':
		print "Started"

	elif obj.type == "GAME_FLAGPICKUP":
		if obj.data['flagid'] == 1 and redFlag.status == 0: redFlag.start()
		elif obj.data['flagid'] == 2 and blueFlag.status == 0: blueFlag.start()

	elif obj.type == "GAME_FLAGRETURN":
		if obj.data['flagid'] == 1: redFlag.reset()
		elif obj.data['flagid'] == 2: blueFlag.reset()

	elif obj.type == "GAME_FLAGCAPTURE":
		if obj.data['flagid'] == 1:
			redFlag.stop()
			api.say('%sRed %sFlag captured in %s%s' % (api.RED, api.YELLOW, api.CYAN ,redFlag.value()))
			redFlag.reset()
		elif obj.data['flagid'] == 2:
			blueFlag.stop()
			api.say('%sBlue %sFlag captured in %s%s' % (api.BLUE, api.YELLOW, api.CYAN ,redFlag.value()))
			blueFlag.reset()
	elif obj.type == "GAME_FLAGRESET":
		if obj.data['flagid'] == 1: redFlag.reset()
		elif obj.data['flagid'] == 2: blueFlag.reset()

def init(A):
	global api
	api = A
	print 'Firing'
	eventListener('init')
	api.addListeners(['GAME_FLAGPICKUP', 'GAME_FLAGDROP', 'GAME_FLAGRETURN', 'GAME_FLAGCAPTURE', 'GAME_FLAGRESET'], eventListener)