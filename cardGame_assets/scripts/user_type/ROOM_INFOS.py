# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class RoomInfos(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		#DEBUG_MSG("RoomInfos.__init__")
		list.__init__(self)
		
	def asDict(self):
		#DEBUG_MSG("RoomInfos.asDict")
		data = {
			"roomKey"		: self[0],
			"name"		    : self[1],
			"intro"			: self[2],
			"playerCount"	: self[3],
			"isPlaying"		: self[4],
			"hasPassword"	: self[5]
		}
		
		return data

	def createFromDict(self, dictData):
		#DEBUG_MSG("RoomInfos.createFromDict,dictData:%s" % dictData)
		self.extend([dictData["roomKey"], dictData["name"], dictData["intro"], dictData["playerCount"], dictData["isPlaying"], dictData["hasPassword"]])
		return self
		
class ROOM_INFOS_PICKLER:
	def __init__(self):
		#DEBUG_MSG("ROOM_INFOS_PICKLER.__init__")
		pass

	def createObjFromDict(self, dct):
		#DEBUG_MSG("ROOM_INFOS_PICKLER.createObjFromDict,dct:%s" % dct)
		return RoomInfos().createFromDict(dct)

	def getDictFromObj(self, obj):
		#DEBUG_MSG("ROOM_INFOS_PICKLER.getDictFromObj,obj:%s" % obj)
		return obj.asDict()

	def isSameType(self, obj):
		#DEBUG_MSG("ROOM_INFOS_PICKLER.isSameType,obj:%s" % obj)
		return isinstance(obj, RoomInfos)

room_info_inst = ROOM_INFOS_PICKLER()

class RoomInfosList(dict):
	"""
	"""
	def __init__(self):
		#DEBUG_MSG("RoomInfosList.__init__")
		"""
		"""
		dict.__init__(self)
		
	def asDict(self):
		#DEBUG_MSG("RoomInfosList.asDict,items:%s" % self.items())
		datas = []
		dct = {"values" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		#DEBUG_MSG("RoomInfosList.createFromDict,dictData:%s" % dictData)
		for data in dictData["values"]:
			self[data[0]] = data
		return self
		
class ROOM_INFOS_LIST_PICKLER:
	def __init__(self):
		#DEBUG_MSG("ROOM_INFOS_LIST_PICKLER.__init__")
		pass

	def createObjFromDict(self, dct):
		#DEBUG_MSG("ROOM_INFOS_LIST_PICKLER.createObjFromDict,dct:%s" % dct)
		return RoomInfosList().createFromDict(dct)

	def getDictFromObj(self, obj):
		#DEBUG_MSG("ROOM_INFOS_LIST_PICKLER.getDictFromObj,obj:%s" % obj)
		return obj.asDict()

	def isSameType(self, obj):
		#DEBUG_MSG("ROOM_INFOS_LIST_PICKLER.isSameType,obj:%s,obj type:%s" % (obj,type(obj)))
		return isinstance(obj, RoomInfosList)

room_info_list_inst = ROOM_INFOS_LIST_PICKLER()