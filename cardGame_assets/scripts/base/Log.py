# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Log(KBEngine.Entity):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		DEBUG_MSG("log init:accountid:%s,action:%s,value:%s,time:%s" % (self.accountId,self.action,self.value,self.time))
		self.writeToDB()

	def destroySelf(self):
		"""
		"""
		DEBUG_MSG("Log base::destroySelf")

		# 销毁base
		DEBUG_MSG("Log base::destroy base")
		self.destroy()

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
		
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)

	def onGetCell(self):
		"""
		KBEngine method.
		entity的cell部分实体被创建成功
		"""
		DEBUG_MSG('Log base::onGetCell: %s' % self.cell)

	def onLoseCell(self):
		"""
		KBEngine method.
		entity的cell部分实体丢失
		"""
		DEBUG_MSG("Log base::onLoseCell: %i" % (self.id))