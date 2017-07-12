#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 17:08:10 2017

@author: lenalee
"""

import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape)
print(x_train.shape)

train_size = x_train.shpae[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch    = x_train(batch_mask)
t_batch    = t_train(batch_mask)
