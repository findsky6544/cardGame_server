# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class BanInfos(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		#DEBUG_MSG("BanInfos.__init__")
		list.__init__(self)
		
	def asDict(self):
		#DEBUG_MSG("BanInfos.asDict")
		data = {
			"dbid"			: self[0],
			"accountId"		: self[1],
			"startTime"		: self[2],
			"finishTime"	: self[3],
			"reason"		: self[4],
			"state"			: self[5]
		}
		
		return data

	def createFromDict(self, dictData):
		#DEBUG_MSG("BanInfos.createFromDict,dictData:%s" % dictData)
		self.extend([dictData["dbid"], dictData["accountId"], dictData["startTime"], dictData["finishTime"], dictData["reason"], dictData["state"]])
		return self
		
class BAN_INFOS_PICKLER:
	def __init__(self):
		#DEBUG_MSG("BAN_INFOS_PICKLER.__init__")
		pass

	def createObjFromDict(self, dct):
		#DEBUG_MSG("BAN_INFOS_PICKLER.createObjFromDict,dct:%s" % dct)
		return BanInfos().createFromDict(dct)

	def getDictFromObj(self, obj):
		#DEBUG_MSG("BAN_INFOS_PICKLER.getDictFromObj,obj:%s" % obj)
		return obj.asDict()

	def isSameType(self, obj):
		#DEBUG_MSG("BAN_INFOS_PICKLER.isSameType,type of obj:%s" % type(obj))
		return isinstance(obj, BanInfos)

ban_info_inst = BAN_INFOS_PICKLER()

class BanInfosList(dict):
	"""
	"""
	def __init__(self):
		#DEBUG_MSG("BanInfosList.__init__")
		"""
		"""
		dict.__init__(self)
		
	def asDict(self):
		#DEBUG_MSG("BanInfosList.asDict,items:%s" % self.items())
		datas = []
		dct = {"values" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		#DEBUG_MSG("BanInfosList.createFromDict,dictData:%s" % dictData)
		for data in dictData["values"]:
			self[data[0]] = data
		return self
		
class BAN_INFOS_LIST_PICKLER:
	def __init__(self):
		#DEBUG_MSG("BAN_INFOS_LIST_PICKLER.__init__")
		pass

	def createObjFromDict(self, dct):
		#DEBUG_MSG("BAN_INFOS_LIST_PICKLER.createObjFromDict,dct:%s" % dct)
		return BanInfosList().createFromDict(dct)

	def getDictFromObj(self, obj):
		#DEBUG_MSG("BAN_INFOS_LIST_PICKLER.getDictFromObj,obj:%s" % obj)
		return obj.asDict()

	def isSameType(self, obj):
		#DEBUG_MSG("BAN_INFOS_LIST_PICKLER.isSameType,obj:%s,obj type:%s" % (obj,type(obj)))
		return isinstance(obj, BanInfosList)

ban_info_list_inst = BAN_INFOS_LIST_PICKLER()