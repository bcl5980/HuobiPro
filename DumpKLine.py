import argparse
import LoadSave as ls

parser = argparse.ArgumentParser(description='DumpKLine')
parser.add_argument('--symbol', default='eosusdt', help='eosusdt/btcusdt/ethusdt/ethbtc')
parser.add_argument('--period', default='1min', help='1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year')
parser.add_argument('--size', type=int, default=200, help='default=200 (1,1000)')

args = parser.parse_args()

ls.save_k(args.symbol, args.period, args.size)