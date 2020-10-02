#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Lenny lin
@contact: lennylin@elongthink.com
@version: 1.0.0
'''

import random
import sys
import subprocess
from typing import List

class LuckyThrow:

    def __init__(self):
        self.four_count = 0
        self.two_count = 0
        self.one_count = 0
        self.three_count = 0
        self.five_count = 0
        self.six_count = 0
        self.luckylist =[]
        self.msg = ""
        self.greeting = "恭喜你！中奖啦！"
        self.big_greeting = "哇噻，中大奖啦！"
        self.biggest_greeting = "哇啊！！！今天运气爆棚，就数你最棒！"
        self.total = 0
        self.prizelist = {1:"一甲第一：状元插金花",2:"一甲第二：状元满堂红",3:"一甲第三：状元遍地锦",
                    4:"一甲第四：状元六勃黑",5:"一甲第五：状元五红",6:"一甲第六：状元五子登科",7:"一甲第七：状元四点红",
                    8:"二甲：对堂（榜眼）",9:"三甲：三红（探花）",10:"四乙：四进（进士）",11:"五丁：二举（举人）",
                    12:"六丙：一秀（秀才）"}

    def countdigit(self):
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        count6=0

        for item in self.luckylist:
            if item == 1:
                count1 += 1
            if item == 2:
                count2 += 1
            if item == 3:
                count3 += 1
            if item == 4:
                count4 += 1
            if item == 5:
                count5 += 1
            if item == 6:
                count6 += 1
        self.four_count = count4
        self.two_count = count2
        self.three_count = count3
        self.one_count = count1
        self.five_count = count5
        self.six_count = count6


    def sumup(self):
        self.total = sum(self.luckylist)

    def throw(self):
        item = 10
        self.luckylist: List[int] = [int(item * random.random()) % 6 + 1 for i in range(6)]

    def prize(self):
        self.countdigit()
        self.sumup()
        msg = ""
        if self.four_count == 6 and self.total == 24:
            msg = self.big_greeting+self.prizelist.get(2)
        elif self.four_count == 5 and self.total == 21:
            msg = self.big_greeting+self.prizelist.get(5)

        elif self.four_count == 4:
            if self.total == 18:
                msg = self.biggest_greeting+self.prizelist.get(1)
            else:
                msg = self.big_greeting+self.prizelist.get(7)
        elif self.four_count == 3:
            msg = self.greeting+self.prizelist.get(9)
        elif self.four_count == 2:
            msg = self.greeting+self.prizelist.get(11)
        elif self.two_count == 6:
            msg = self.big_greeting+self.prizelist.get(4)
        elif self.one_count ==6:
            msg = self.big_greeting+self.prizelist.get(4)
        elif self.three_count ==6:
            msg = self.big_greeting+self.prizelist.get(4)
        elif self.five_count ==6:
            msg = self.big_greeting+self.prizelist.get(4)
        elif self.six_count ==6:
            msg = self.big_greeting+self.prizelist.get(4)
        elif self.one_count ==5:
            msg = self.big_greeting + self.prizelist.get(6)
        elif self.two_count == 5:
            msg = self.big_greeting + self.prizelist.get(6)
        elif self.throw() ==5:
            msg = self.big_greeting + self.prizelist.get(6)
        elif self.five_count ==5:
            msg = self.big_greeting + self.prizelist.get(6)
        elif self.six_count == 5:
            msg = self.big_greeting + self.prizelist.get(6)
        elif self.one_count ==4:
            msg = self.greeting + self.prizelist.get(10)
        elif self.two_count == 4:
            msg = self.greeting+self.prizelist.get(10)
        elif self.three_count == 4:
            msg = self.greeting + self.prizelist.get(10)
        elif self.five_count ==4:
            msg = self.greeting + self.prizelist.get(10)
        elif self.six_count ==4:
            msg = self.greeting + self.prizelist.get(10)
        elif self.total == 6:
            msg = self.big_greeting+self.prizelist.get(3)
        elif self.one_count == 1 and self.two_count ==1 and self.three_count ==1 and self.total == 21:
            msg = self.greeting+self.prizelist.get(8)
        elif self.four_count == 1:
            msg = self.greeting+self.prizelist.get(12)
        else:
            msg ="很遗憾，没有中奖啊，希望下次好运哦！"
        return msg

    def display_result(self):
        print(self.luckylist)
        self.msg = self.prize()
        print(self.msg)

def talk(msg):
    subprocess.run(["say",msg])

def main():

    luckythrow = LuckyThrow()
    luckythrow.throw()
    luckythrow.prize()
    luckythrow.display_result()

    try:
        talk(luckythrow.msg)
    except Exception:
        print("抱歉，语音播报功能不可用！")

    exit(0)
if __name__ == "__main__": main()
