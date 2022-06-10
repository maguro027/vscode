import collections
import math
from msvcrt import getch
import msvcrt
import time

class Load_Bar():

    off_bar = '□'
    on_bar = '■'

    def __init__(self, size, mode):
        self.bar_tepy_on = '■'
        self.bar_tepy_off = '□'

        self.size = size/10
        self.mode = mode
        self.i = 0
        pro_bar = self.bar_tepy_off * 20
        if mode == '':
            print('\r[{0}] {1} % {2}'.format(pro_bar, self.i, ''), end='')
        elif mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,
                  self.i, size, ''), end='')

    def add(self, txt):
        self.i = self.i + 1
        progress = (self.i/self.size)*100
        pro_size_1 = math.floor(progress//5)
        pro_size_2 = 20-math.floor(progress//5)
        pro_bar = (self.bar_tepy_on * pro_size_1) + \
            (self.bar_tepy_off * pro_size_2)
        if self.mode == '':
            print('\r[{0}] {1} % {2}'.format(
                pro_bar, format(progress, '.3f'), txt), end='')
        elif self.mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,
                  self.i, self.size, txt), end='')

    def adds(self, amount, txt):
        self.i = self.i + (amount/10)
        progress = (self.i/self.size)*100
        pro_size_1 = math.floor(progress//5)
        pro_size_2 = 20-math.floor(progress//5)
        pro_bar = (self.bar_tepy_on * pro_size_1) + \
            (self.bar_tepy_off * pro_size_2)
        if self.mode == '':
            print('\r[{0}] {1} % {2}'.format(
                pro_bar, format(progress, '.3f'), txt), end='')
        elif self.mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,
                  format(self.i, '.1f'), self.size, txt), end='')
        if self.i >= self.size+0.1:

            print('[Error]Over Load')

    def set(self, amount, txt):
        self.i = amount
        progress = (self.i/self.size)*100
        pro_size_1 = math.floor(progress//5)
        pro_size_2 = 20-math.floor(progress//5)
        pro_bar = (self.bar_tepy_on * pro_size_1) + \
            (self.bar_tepy_off * pro_size_2)
        if self.mode == '':
            print('\r[{0}] {1} % {2}'.format(
                pro_bar, format(progress, '.3f'), txt), end='')
        elif self.mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,
                  self.i, self.size, txt), end='')

class Blind():
    # Blind-Level
    B_Level = 0
    #Blind-time (s)
    B_time = 10000
    # Level-SB-BB-AN
    Level = {'0': 'BB-200/SB-100/AN-50',
             '1': 'BB-300/SB-150/AN-50',
             '2': 'BB-600/SB-300/AN-100',
             '3': 'BB-800/SB-400/AN-150',
             '4': 'BB-900/SB-500/AN-200',
             '5': 'BB-1300/SB-600/AN-300',
             '6': 'BB-2000/SB-1000/AN-400',
             '7': 'BB-4000/SB-1500/AN-500',
             '8': 'BB-5000/SB-2000/AN-1000',
             '9': 'BB-7000/SB-4000/AN-2000'} 

    while True:
        stand = input('Stand by OK typing [start] Do you need help?[help]')
        if stand == 'help':
            print('↑     :レベルアップ')
            print('↓     :レベルダウン')
            print('←     :-10s')
            print('→     :+10s')
            print('space :+一時停止')

        if stand == 'start':
            break

    creat_ = Load_Bar(B_time, 'count')
    c = collections.Counter(Level)

    ap_1 = 0
    ap_2 = 0
    while ap_1 == 0:

        if len(c) <= B_Level:
            a = input('何かキーを打ち込むと再開します')
            break

        while ap_2 == 0:
            if creat_.i >= creat_.size:
                creat_.set(0, 'Level Up                          ')
                print()
                B_Level = B_Level+1
                break

            if msvcrt.kbhit():
                key = int(ord(getch()))
                if key == 32:
                    a = input('何かキーを打ち込むと再開します')
                if key == 72:
                    creat_.adds(100, 'TIME+10                         ')
                    print()
                if key == 80:
                    creat_.adds(-100, 'TIME-10                        ')
                    print()
                    continue
                if key == 77:
                    creat_.adds(0, 'Level Up                          ')
                    creat_.set(0, 'Level Up                          ')
                    if len(c) <= B_Level:
                        print('NO')
                        continue
                    else:
                        B_Level = B_Level+1
                        print()
                        continue
                if key == 75:
                    creat_.set(0, 'Level Down                        ')
                    if B_Level <= 0:
                        print('NO')
                        continue
                    else:
                        B_Level = B_Level-1
                        print()
                        continue
            else:
                time.sleep(0.1)
                creat_.adds(1,'Level-'+str(B_Level)+' '+Level[str(B_Level)])