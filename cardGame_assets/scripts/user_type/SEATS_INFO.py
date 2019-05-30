# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class PlayerInfos(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		DEBUG_MSG("PlayerInfos.__init__")
		list.__init__(self)
		
	def asDict(self):
		DEBUG_MSG("PlayerInfos.asDict")
		data = {
			"id"			: self[0],
			"name"			: self[1],
			"winCount"		: self[2],
			"loseCount"		: self[3],
			"isReady"		: self[4],
			"seatIndex"		: self[5],
			"isRoomMaster"	: self[6]
		}
		
		return data

	def createFromDict(self, dictData):
		DEBUG_MSG("PlayerInfos.createFromDict,dictData:%s" % dictData)
		self.extend([dictData["id"], dictData["name"], dictData["winCount"], dictData["loseCount"], dictData["isReady"], dictData["seatIndex"], dictData["isRoomMaster"]])
		return self
		
class PLAYER_INFOS_PICKLER:
	def __init__(self):
		DEBUG_MSG("PLAYER_INFOS_PICKLER.__init__")
		pass

	def createObjFromDict(self, dct):
		DEBUG_MSG("PLAYER_INFOS_PICKLER.createObjFromDict,dct:%s" % dct)
		return PlayerInfos().createFromDict(dct)

	def getDictFromObj(self, obj):
		DEBUG_MSG("PLAYER_INFOS_PICKLER.getDictFromObj,obj:%s" % obj)
		return obj.asDict()

	def isSameType(self, obj):
		DEBUG_MSG("PLAYER_INFOS_PICKLER.isSameType,type of obj:%s" % type(obj))
		return isinstance(obj, PlayerInfos)

player_info_inst = PLAYER_INFOS_PICKLER()

class SeatsInfoList(dict):
	"""
	"""
	def __init__(self):
		#DEBUG_MSG("SeatsInfoList.__init__")
		"""
		"""
		dict.__init__(self)
		
	def asDict(self):
		#DEBUG_MSG("SeatsInfoList.asDict,items:%s" % self.items())
		datas = []
		dct = {"values" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		#DEBUG_MSG("SeatsInfoList.createFromDict,dictData:%s" % dictData)
		for data in dictData["values"]:
			self[data[0]] = data
		return self
		
class SEATS_INFO_PICKLER:
	def __init__(self):
		#DEBUG_MSG("SEATS_INFO_PICKLER.__init__")
		pass

	def createObjFromDict(self, dct):
		#DEBUG_MSG("SEATS_INFO_PICKLER.createObjFromDict,dct:%s" % dct)
		return SeatsInfoList().createFromDict(dct)

	def getDictFromObj(self, obj):
		#DEBUG_MSG("SEATS_INFO_PICKLER.getDictFromObj,obj:%s" % obj)
		return obj.asDict()

	def isSameType(self, obj):
		#DEBUG_MSG("SEATS_INFO_PICKLER.isSameType,obj:%s,obj type:%s" % (obj,type(obj)))
		return isinstance(obj, SeatsInfoList)

seats_info_inst = SEATS_INFO_PICKLER()