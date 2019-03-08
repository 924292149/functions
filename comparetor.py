#比较器
dictSmaple1 = {"1":"4","name":"MaXiangfei","bornCity":"Fengcheng","school":{"priSchool":"Dongfanghong1","midSchool":"3rdMidSchool","highSchool":"1stSchool"},"workExp":{"LenovoDBG":{"2012":"systemComTeam","2013":"BIOSTeam"},"LenovoR":"SSDTeam"}}	
dictSmaple2 = {"2":"3","name":"MaXiangfei","bornCity":"Fengcheng","school":{"priSchool":"Dongfanghong2","midSchool":"3rdMidSchool","highSchool":"1stSchool"},"workExp":{"LenovoDBG":{"2012":"systemComTeam","2013":"BIOSTeam"},"LenovoR":"SSDTeam"}}	
'''
说明：此类用于比较两个嵌套字典的异同，包含以下特性：
1.输入：
	oldDict：旧字典
	newDict：新字典
2.自有变量：
	self.oldDict，经转化过的旧字典，只有一层
	self.newDict，经转化过的新字典，只有一层
3.自有方法：
	switchDict(self,dictIpt):输入嵌套字典，输出只有一层的字典
	isNestDict(self,dictIpt):判断字典是否是嵌套的
	degradeDict(self,dictIpt):给字典降一级(减少一个维度)
	compareDict(self):比较新旧两个字典，返回三个列表：增加的键，减少的键，值有变化的键
	getVlaue(self,key):输入键名，返回新旧字典对应的值
'''
class Comparator():
	def __init__(self,oldDict,newDict):
		self.oldDict = self.switchDict(oldDict)
		self.newDict = self.switchDict(newDict)
	def switchDict(self,dictIpt):
		index = 1
		dictIpt = {1:dictIpt}
		while self.isNestDict(dictIpt[index]):
			index = index + 1
			dictIpt[index] = self.degradeDict(dictIpt[index-1])
		return dictIpt[index]
	def isNestDict(self,dictIpt):
		for key in dictIpt:
			if isinstance(dictIpt[key],dict):
				return True
		return False
	def degradeDict(self,dictIpt):
		dictOpt = {}
		for key in dictIpt:
			if isinstance(dictIpt[key],dict):
				for keySub in dictIpt[key]:
					dictOpt[key+'-'+keySub] = dictIpt[key][keySub]
			else:
				dictOpt[key] = dictIpt[key]
		return dictOpt	
	def compareDict(self):
		moreKey =[]
		lessKey =[]
		diffKey =[]
		for key in self.oldDict:
			if not self.newDict.get(key):
				lessKey.append(key)
			else:
				if self.newDict[key] != self.oldDict[key]:
					diffKey.append(key)
		for key in self.newDict:
			if not self.oldDict.get(key):
				moreKey.append(key)
		return [moreKey,lessKey,diffKey]
	def getVlaue(self,key):
		return self.oldDict.get(key),self.newDict.get(key)
new = Comparator(dictSmaple1,dictSmaple2)
dictsss = new.switchDict(dictSmaple1)
for key in dictsss:
	print(key + ':'+ dictsss[key])
	
print(new.compareDict())
print(new.getVlaue("name"))