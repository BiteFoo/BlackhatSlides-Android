# coding:utf8
'''
@File    :   gen.py
@Author  :   Loopher 
@Version :   1.0
@date    :    2023/10/20 16:25:31
@License :   (C)Copyright 2020-2021,Loopher
@Desc    :   自动生成table数据
'''
import os


def iter_pdf(p):
    # print("p = ", p)
    for _, _, fs in os.walk(p):
        for f in fs:
            if f.endswith('.pdf'):
                yield f


def gen_table():
    lines = []
    for f in iter_pdf(os.getcwd()):
        print("|"+f+"|")


    #     lines.append("|")
    #     lines.append("|"+f+"|")
    # print("")
if __name__ == '__main__':
    gen_table()
