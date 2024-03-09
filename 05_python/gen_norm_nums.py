#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time ：2024/3/9 20:18 
@Auth ：xana lee
@File ：gen_norm_nums.py.py
@IDE ：PyCharm
@Motto ：ABC(Always Be Coding)
"""
import sys
from random import *
from statistics import *

fileName, size, mu, sd = sys.argv[1:]
size = int(size)
mu = float(mu)
sd = float(sd)
f = open(fileName, 'w')
num_ls = []
for i in range(size):
    num_i = gauss(mu=mu, sigma=sd)
    f.write(str(num_i))
    f.write('\n')
    num_ls.append(num_i)
f.close()
print('Size:   %s' % size)
print('Mean:   requested=%s, generated=%s' % (mu, mean(num_ls)))
print('Stddev: requested=%s, generated=%s' % (sd, stdev(num_ls)))
