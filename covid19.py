#coding: utf-8
import requests
import json
import time
time.sleep(1)
url="https://covid19-brazil-api.now.sh/api/report/v1"
http=requests.get(url)
check=http.ok
if check == True:
	data=json.loads(http.text)
	print(data["data"][0]["state"])
	print(data["data"][0]['cases'], "casos")
	print(data["data"][0]['deaths'], "mortes")
	print(data["data"][0]['suspects'], "suspeitos")
else:
	print("Falha ao iniciar Script")
	exit()

