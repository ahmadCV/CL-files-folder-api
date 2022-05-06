import requests

audio = open('true.mp3', 'rb')
files = {'file': audio}
dat = {'folder': '2'}
response = requests.post('http://192.168.100.106:5000/send', files=files, data=dat)
print(response)
