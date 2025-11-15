import requests
import json
from os import system

clear = lambda: system('cls||clear')

system('title Eirene Ip-Checker')
clear()


ip_adress = input('Enter ip adress: ')

url = f"https://ipinfo.io/widget/demo/{ip_adress}"

response = requests.get(url)
json_response = json.loads(response.text)

print('\nInformation:')
print('Ip: ' + json_response["data"]["ip"])
print('Hostname: ' + json_response["data"]["hostname"])
print('City: ' + json_response["data"]["city"])
print('Region: ' + json_response["data"]["region"])
print('Location: ' + json_response["data"]["loc"])
print('Zip-Code: ' + json_response["data"]["postal"])
print('Timezone: ' + json_response["data"]["timezone"])

print('\nPrivacy:')
if json_response["data"]["privacy"]["vpn"] == False:
    print('Vpn Status: False')
elif json_response["data"]["privacy"]["vpn"] == True:
    print('Vpn Status: True')
else:
    print('Vpn Status: 404 Not Found')

if json_response["data"]["privacy"]["proxy"] == False:
    print('Proxy Status: False')
elif json_response["data"]["privacy"]["proxy"] == True:
    print('Proxy Status: True')
else:
    print('Proxy Status: 404 Not Found')

if json_response["data"]["privacy"]["tor"] == False:
    print('Tor Status: False')
elif json_response["data"]["privacy"]["tor"] == True:
    print('Tor Status: True')
else:
    print('Tor Status: 404 Not Found')
