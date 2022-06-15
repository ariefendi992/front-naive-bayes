
import datetime
import requests
from dateutil import parser
testeddate = '2022-04-11 17:26:18'
dt_obj = datetime.datetime.strptime(testeddate, '%Y-%m-%d %H:%M:%S')
dt_str = datetime.datetime.strftime(dt_obj, '%d-%m-%Y %H:%M:%S')
print(dt_str)



# base_url = 'http://192.168.1.8:5000'

# url = base_url + ('/auth/get-uid?id=2')

# r = requests.get(url).json()

# print(r)

from app.url import base_url 

url = base_url + '/auth/get-all'
req  = requests.get(url).json()
resp = req['data']

for i in resp:
    print(i['created_at'])

dt_obj2 = i['created_at']
parseTime = parser.parse(dt_obj2)
# dt_str = datetime.datetime.isoformat(dt_obj2)
# print('dt str = ', dt_str)
tahun = str(parseTime)[:4]
bulan = str(parseTime)[5:7]
tanggal = str(parseTime)[8:10]
print('parse time = ',parseTime)
print(tahun)
print(bulan)
print(tanggal)


url_stambuk = base_url + '/auth/get-stambuk'
req = requests.get(url_stambuk)
resp2 = req.json().get('data')



for i in resp2:
    if '17024014159' in i['stambuk']:
        print('ada')
    else:
        print('tidak ada')
