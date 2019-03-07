def switchDictToStr(filePath):
	with open(filePath,'r') as f:
		tempStr = f.read()#get sample string
		tempStr = tempStr.replace('{','',1)#delete first { , to forbid too much intent
		tempStr = tempStr.replace('"','')
		tempStr = tempStr.replace(',','\n')
		tempStr = tempStr.replace('{','{\n')
		tempList = tempStr.split('\n')
		theIndents = '\t'#set indent
		indentsCnt = 0
		newTmepList = []
		for i in tempList:
			i = theIndents*indentsCnt + i 
			indentsLeft = i.count('{')
			indentsRight = i.count('}')
			indentsCnt = indentsCnt + indentsLeft - indentsRight
			newTmepList.append(i)
		
		tempStr = '\n'.join(newTmepList)
		
		tempStr = tempStr.replace('{','')
		tempStr = tempStr.replace('}','')
		return tempStr
filepath = 'dictSample.txt'
print(switchDictToStr(filepath))