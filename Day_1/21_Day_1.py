import json
import requests
from urllib.request import urlopen

#URL to a free coronavirus API
with urlopen("https://api.covid19api.com/summary") as response:
    source = response.read()

#Loading the json format to a python readable format
data = json.loads(source)
#data = requests.get("https://api.covid19api.com/summary").json()
#print(json.dumps(data['Countries'], indent = 2))

#Parsing through the objects and printing the country 
#and the country's recovered count
for item in data["Countries"]:
    print(str(item['Country'])+" "+str(item['TotalRecovered']))
    