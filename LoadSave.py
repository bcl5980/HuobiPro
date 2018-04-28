import HuobiServices as hs
import json

__all__ = [
    'save_k',
    'load_k',
]

def save_k(symbol, period, size):
    kline = hs.get_kline(symbol, period, size)
    name = '{}_{}_{}.json'.format(symbol, period, size)
    with open(name, 'w') as file:
        json.dump(kline, file)

def load_k(filename):
    with open(filename, 'r') as file:
        kline = json.load(file)
    return kline