import json
import os
class JsonObj():#json related
	def __init__(self,jsonFileName):
		self.jsonFileName = jsonFileName
		
	def jsLoad(self):
		jsDict = {}
		with open(self.jsonFileName,'r',encoding='utf-8') as jsFile:
			jsDict = json.load(jsFile)
		return jsDict
	
	def jsDump(self,jsDict):
		with open(self.jsonFileName,'w',encoding='utf-8') as jsFile:
			json.dump(jsDict,jsFile)

	def jsAdd(self,jsKey,jsValue):
		if os.path.exists(self.jsonFileName):
			jsDict = self.jsLoad()
		else:
			jsDict = {}
		jsDict[jsKey] = jsValue
		self.jsDump(jsDict)
		
	def jsDelete(self,jsKey):
		jsDict = self.jsLoad()
		del jsDict[jsKey]#need fix error correct
		self.jsDump(jsDict)

	def jsCheck(self,jsKey):
		jsDict = self.jsLoad()
		return jsDict[jsKey]
		
class TimeManage():
	
