import urllib.request
import json
# 获取 k线数据,

class get_k:
     # k线单位 1分钟
    def get_1m():
     url= 'https://www.binancezh.com/api/v3/klines?symbol=ETHUSDT&interval=1m'
     response = urllib.request.urlopen(url)
     text = response.read().decode('utf-8')
     result = json.loads(text)
     data=[]


     for item in enumerate(result):
         # object=item.rename(columns={0: 'time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
         item=item[1]
         object={
             'time':item[0],
             'open':item[1],
             'high':item[2],
             'low':item[3],
             'close':item[4],
             'volume':item[5]
         }
         data.append(object)
     print(data)
     return  result



if __name__ == '__main__':
    get_1m()
