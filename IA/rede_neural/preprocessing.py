# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:40:18 2019

@author: jp-ad
"""


def min_max_scaler(xmin, xmax, x):
    return 1 - ((x - xmin) / (xmax - xmin))
