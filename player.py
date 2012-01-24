import database
import auth
import time 
from config import securityConfig

class Player():
	def __init__(self, uid, data, api):
		self.uid = int(uid)
		self.cid = None #<<< get from the db
		self.data = data
		self.group = 0
		self.status = None
		self.api = api
		self.nick = None

		self.score = [0,0]
		try:
			self.name = None
			self.ip = None
			self.team = None
			self.model = None
			self.sex = None
			self.headmodel = None
			self.team_model = None
			self.team_headmodel = None
			self.funred = None
			self.funblue = None
			self.raceRed = None
			self.raceBlue = None
			self.color1 = None
			self.color2 = None
			self.cg_predictitems = None
			self.cg_anonymous = None
			self.cl_guid = None
			self.cg_rgb = None
			self.cg_physics = None
			self.weapmodes = None
			self.gear = None
			self.teamtask = None
			self.handicap = None
			self.rate = None
			self.snaps = None
			self.ut_timenudge = None
			self.setData(self.data)
		except Exception, e:
			print e

		self.client = database.Client(nick=self.name, ip=self.ip, guid=self.cl_guid, db=database.db)
		self.client.clientJoin()
		self.cid = self.client.__id__
		self.group = self.client.cgroup

	def checkAuth(self): #@DEV Fix this some
		self.client.push()
		self.client.pull()
		self.cid = self.client.__id__
		self.group = self.client.cgroup

	def setData(self, data):
		if 'name' in data.keys():
			data['name'] = data['name'].lower()
		for i in data.keys(): #Strip line endings
			data[i] = data[i].strip()
		self.__dict__.update(data)
	
	def updateData(self, data):
		if 'name' in data.keys():
			data['name'] = data['name'].lower()
		if 'team' in data.keys():
			if data['team'] != self.team:
				print 'Fired change team from updateData'
				self.api.B.eventFire('CLIENT_SWITCHTEAM', {'client':self.uid, 'toteam':data['team'], 'fromteam':self.team})
		self.setData(data)
