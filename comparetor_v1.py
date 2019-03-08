# #遍历一个嵌套字典
dictSmaple1 = {"1":"4","name":"MaXiangfei","bornCity":"Fengcheng","school":{"priSchool":"Dongfanghong","midSchool":"3rdMidSchool","highSchool":"1stSchool"},"workExp":{"LenovoDBG":{"2012":"systemComTeam","2013":"BIOSTeam"},"LenovoR":"SSDTeam"}}	
dictSmaple2 = {"2":"3","name":"MaXiangfei","bornCity":"Fengcheng","school":{"priSchool":"Dongfanghong2","midSchool":"3rdMidSchool","highSchool":"1stSchool"},"workExp":{"LenovoDBG":{"2012":"systemComTeam","2013":"BIOSTeam"},"LenovoR":"SSDTeam"}}	
class Comparator():
	def isNestDict(dictIpt):#如果目标字典有嵌套，则返回真
			for key in dictIpt:
				if isinstance(dictIpt[key],dict):
					return True
			return False
			
	def degradeDict(dictIpt):#字典降维
		dictOpt = {}
		for key in dictIpt:
			if isinstance(dictIpt[key],dict):
				for keySub in dictIpt[key]:
					dictOpt[key+'-'+keySub] = dictIpt[key][keySub]
			else:
				dictOpt[key] = dictIpt[key]
		return dictOpt	
		
	def switchDict(dictIpt):#字典转换函数
		index = 1
		while isNestDict(dictIpt[index]):
			index = index + 1
			dictIpt[index] = degradeDict(dictIpt[index-1])
		return dictIpt[index]
	def compareDict(self,dict1,dict2):#比较两个字典，并将不同返回
	

		moreKey =[]
		lessKey =[]
		diffKey =[]
		dictOld = switchDict({1:dict1})
		dictNew = switchDict({1:dict2})
		theOldDict = dictOld
		theNewDict = dictNew
		print(theOldDict)
		
		for key in dictOld:
			if not dictNew.get(key):
				lessKey.append(key)
			else:
				if dictNew[key] != dictOld[key]:
					diffKey.append(key)
		for key in dictNew:
			if not dictOld.get(key):
				moreKey.append(key)
		return [moreKey,lessKey,diffKey]

new = Comparator()
new.compareDict(dictSmaple1,dictSmaple2)
