import HuobiServices
import time
import json

__all__ = [
    'get_depth',
    'get_depthfromjson',
    'get_k',
    'get_kfromjson',
]

def get_depthfromjson(depthjson):
    tick = depthjson['tick']
    ts = depthjson['ts']
    tstime = time.ctime(ts / 1000)
    ret = []
    for v in tick['bids']:
        ret.append(v)
    for v in tick['asks']:
        ret.append(v)
    return ret, tstime

def get_depth(symbol, step):
    depth = HuobiServices.get_depth(symbol, step)
    return get_depthfromjson(depth)

def get_kfromjson(kjson):
    datas = kjson['data']
    ts = kjson['ts']
    tstime = time.ctime(ts / 1000)
    ret = []
    for sd in datas:
        ld = []
        ld.append(sd['open'])
        ld.append(sd['close'])
        ld.append(sd['low'])
        ld.append(sd['high'])
        ld.append(sd['vol'])
        ld.append(sd['amount'])
        ret.append(ld)
    ret.reverse()
    return ret, tstime

def get_k(symbol, period, size):
    kline = HuobiServices.get_kline(symbol, period, size=size)
    return get_kfromjson(kline)
