import json 
json_info = "{'age': '12'}"
file = open('1.json','w',encoding='utf-8')
json.dump(json_info,file)