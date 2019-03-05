import json
import os
class JsonObj():#json related
	def __init__(self,jsonFileName):
		self.jsonFileName = jsonFileName
		pass
	
	def jsAdd(self,jsKey,jsValue):#add a pair of 'key' & 'value' in jsFile
		jsDict = {}
		if os.path.exists(self.jsonFileName):
			with open(self.jsonFileName,'r',encoding='utf-8') as jsFile:
				jsDict = json.load(jsFile)
		jsDict[jsKey] = jsValue
		with open(self.jsonFileName,'w',encoding='utf-8') as jsFile:
			json.dump(jsDict,jsFile)

	def jsDelete(self,jsKey):
		jsDict = {}
		with open(self.jsonFileName,'r',encoding='utf-8') as jsFile:
			jsDict = json.load(jsFile)
		del jsDict[jsKey]#need fix error correct
		with open(self.jsonFileName,'w',encoding='utf-8') as jsFile:
			json.dump(jsDict,jsFile)

	def jsCheck(self,jsKey):
		jsDict = {}
		with open(self.jsonFileName,'r',encoding='utf-8') as jsFile:
			jsDict = json.load(jsFile)
		return jsDict[jsKey]
		
	def jsCheckAll(self):
		jsDict = {}
		with open(self.jsonFileName,'r',encoding='utf-8') as jsFile:
			jsDict = json.load(jsFile)
		return jsDict
		
		
new = JsonObj('this_is_a_file')
new.jsAdd('this_is_a_key','this_is_a_value')
print(new.jsCheckAll())
