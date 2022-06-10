import math
import time

class Load_Bar():

    off_bar = '□'
    on_bar  = '■'

    def __init__(self, size, mode):
        self.bar_tepy_on  = '■'
        self.bar_tepy_off = '□'
        
        self.size = size
        self.mode = mode
        self.i = 0
        pro_bar = self.bar_tepy_off * 20
        if mode == '':
            print('\r[{0}] {1} % {2}'.format(pro_bar, self.i, ''), end='')
        elif mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,self.i, size, ''), end='')

    def add(self, txt):
        self.i = self.i + 1
        progress = (self.i/self.size)*100
        pro_size_1 = math.floor(progress//5)
        pro_size_2 = 20-math.floor(progress//5)
        pro_bar = (self.bar_tepy_on * pro_size_1) + (self.bar_tepy_off * pro_size_2)
        if self.mode == '':
            print('\r[{0}] {1} % {2}'.format(pro_bar, format(progress, '.3f'), txt), end='')
        elif self.mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,self.i, self.size, txt), end='')

    def adds(self,amount, txt):
        self.i = self.i + amount
        progress = (self.i/self.size)*100
        pro_size_1 = math.floor(progress//5)
        pro_size_2 = 20-math.floor(progress//5)
        pro_bar = (self.bar_tepy_on * pro_size_1) + (self.bar_tepy_off * pro_size_2)
        if self.mode == '':
            print('\r[{0}] {1} % {2}'.format(pro_bar, format(progress, '.3f'), txt), end='')
        elif self.mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,self.i, self.size, txt), end='')
        if self.i+1>=self.size:

            print('[Error]Over Load')

    def set(self,amount, txt):
        self.i =  amount
        progress = (self.i/self.size)*100
        pro_size_1 = math.floor(progress//5)
        pro_size_2 = 20-math.floor(progress//5)
        pro_bar = (self.bar_tepy_on * pro_size_1) + ('  ' * pro_size_2)
        if self.mode == '':
            print('\r[{0}] {1} % {2}'.format(pro_bar, format(progress, '.3f'), txt), end='')
        elif self.mode == 'count':
            print('\r[{0}] {1}/{2} {3}'.format(pro_bar,self.i, self.size, txt), end='')

class Load():
    def now(*classs):
        creat_ = Load_Bar(len(classs),'')
        for num in range(len(classs)):
            creat_.add(classs[num])

    def test(i):
        print(i)
        creat_ = Load_Bar(i, 'count')
        for num in range(i):
            time.sleep(0.001)
            creat_.add(i)
        print('')
        creat__ = Load_Bar(i, '')
        for num in range(i):
            time.sleep(0.001)
            creat__.add(i)
        print('')

        creat___ = Load_Bar(6000, 'count')
        for num in range(i):
            if creat___.i>=creat___.size:
                break
            time.sleep(0.001)
            creat___.adds(53.1656,'')
         
        print('')