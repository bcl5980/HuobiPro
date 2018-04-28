import numpy as np
import talib as ta
import time
import HuobiWrap as hw
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import matplotlib.pyplot as plt

fups = 0
fasterPeriod = 5
slowerPeriod = 10

def buy(val):
    print ('crossdown：{:.5f}'.format(val))

def sell(val):
    print ('crossup：{:.5f}'.format(val))

def kjob():
    global fups, fasterPeriod, slowerPeriod
    klist, ts = hw.get_k('eosusdt','1min',20)
    print (ts)
    k = np.transpose(np.array(klist),(1,0))
    mafaster = ta.SMA(k[1], timeperiod=fasterPeriod)
    maslower = ta.SMA(k[1], timeperiod=slowerPeriod)
    print ('ma5：{:.5f} ma10: {:.5f} cur: {:.5f}'.format(mafaster[-1], maslower[-1], k[1][-1]))
    if fups == 0:
        if mafaster[-1] > maslower[-1]:
            fups = 1
        else:
            fups = -1
    elif fups == 1:
        if mafaster[-1] < maslower[-1]:
            buy(k[1][-1])
            fups = -1
    elif fups == -1:
        if mafaster[-1] > maslower[-1]:
            sell(k[1][-1])
            fups = 1

if __name__ == '__main__':
    # BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(kjob, 'interval', seconds=30)
    scheduler.start()