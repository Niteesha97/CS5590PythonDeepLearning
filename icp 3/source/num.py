# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 17:27:03 2019

@author: Niteesha
"""

import numpy as np
x = np.random.randint(0, 20, 15)
print(x)
print("frequent value is:")
a=np.bincount(x)
print(a.argmax())
