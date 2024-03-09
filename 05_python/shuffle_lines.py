#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time ：2024/3/9 21:30 
@Auth ：xana lee
@File ：shuffle_lines.py
@IDE ：PyCharm
@Motto ：ABC(Always Be Coding)
"""
import sys
from random import shuffle

inFileName, outFileName = sys.argv[1:]
i_f = open(inFileName, 'r')
line_ls = i_f.readlines()
shuffle(line_ls)
o_f = open(outFileName, 'w')
for l in line_ls:
    o_f.write(l)
o_f.close()
