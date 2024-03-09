#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time ：2024/3/5 14:31 
@Auth ：xana lee
@File ：my_script.py
@IDE ：PyCharm
@Motto ：ABC(Always Be Coding)
"""
import sys

if __name__ == "__main__":                  # a suggested way to define the main part of a script
    print("Hello, world!")
    for a in sys.argv:                      # sys.argv contains the script name
        print(a)                            # and additional arguments
