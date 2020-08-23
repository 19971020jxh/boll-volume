import pandas as pd
import urllib.request
import json

import numpy as np
# 绘图
import matplotlib.pyplot as plt

def get_1m():
    url = 'https://www.binancezh.com/api/v3/klines?symbol=ETHUSDT&interval=1m'
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    result = json.loads(text)

    time = []
    open=[]
    high=[]
    low=[]
    close=[]
    volume=[]

    for item in enumerate(result):
        # object=item.rename(columns={0: 'time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
        item = item[1]
        time.append(item[0])
        open.append(item[1])
        high.append(item[2])
        low.append(item[3])
        close.append(item[4])
        volume.append(item[5])
    # print(data)
    data = {
        'time': time,
        'open': open,
        'high': high,
        'low': low,
        'close': close,
        'volume': volume
    }

    return data

def boll(data):
    df = pd.DataFrame(data)
    paras = [100, 2]
    n = paras[0]
    m = paras[1]
    # 计算均线
    df['median'] = df['close'].rolling(n, min_periods=1).mean()

    # 计算上轨、下轨道
    df['std'] = df['close'].rolling(n, min_periods=1).std(ddof=0)  # ddof代表标准差自由度
    df['upper'] = df['median'] + m * df['std']
    df['lower'] = df['median'] - m * df['std']
    # print(df['lower'])

    #画图
    # 将计算的数据合并到DataFrame
    df = df.assign(close=pd.Series(df['close'], index=df.index))
    df = df.assign(boll=pd.Series(df['median'], index=df.index))
    df = df.assign(upper=pd.Series(df['upper'], index=df.index))
    df = df.assign(lower=pd.Series(df['lower'], index=df.index))
    # print(df['收盘价'])
    # print(df['中界线'])
    # print(df['阻力线'])
    # print(df['支撑线'])

    # 绘图
    ax = plt.figure()
    # 设定y轴标签
    # ax.ylabel = '%s price in ￥' % ('ETH')

    df['close'].astype(float).plot(color='k', lw=1., legend=True)
    df['boll'].astype(float).plot(color='b', lw=1., legend=True)
    df['upper'].astype(float).plot(color='r', lw=1., legend=True)
    df['lower'].astype(float).plot(color='g', lw=1., legend=True)
    plt.show()
    pass


if __name__ == '__main__':
    boll(get_1m())
    pass