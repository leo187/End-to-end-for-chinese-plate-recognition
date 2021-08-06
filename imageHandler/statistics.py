import collections
import os
from configparser import ConfigParser
from random import random

import matplotlib.pyplot as plt
import numpy

if __name__ == '__main__':
    type = 1
    path1 = '/Users/xuejian/Desktop/unet_datasets/mutil/'
    size = 8
    nameStr = ''
    if(type == 1):
        length = 0
        for index in range(55):
                path = path1 + 'multi' + str(index) + '/'
                pic_name = sorted(os.listdir(path))
                n = len(pic_name)
                for i in range(n):
                    if ('DS_Store' not in pic_name[i] and len(pic_name[i].split('.')[0])==size):
                        nameStr +=pic_name[i].split('.')[0]
                        length = 1+length
    obj = collections.Counter(nameStr)
    print(obj)
    print('数量' + str(length))

    plt.rcParams['font.family'] = ['Heiti TC']
    plt.tick_params(axis='x', labelsize=6)  # 设置x轴标签大小

    plt.bar(obj.keys(), obj.values())
    plt.title('plate')

    plt.figure(figsize=(15, 4))  # 设置画布大小
    plt.show()
