import os
import cv2
import numpy as np
from configparser import ConfigParser
from conda.cli import main

# 将json文件label转换为到data文件夹
n = 112  # n为总共标注的图片数
ini_file = "./config.ini"
cfg = ConfigParser()
cfg.read(ini_file)
path = cfg['router']['labelme'].replace("\'","")

# for i in range(n):
#    os.system('labelme_json_to_dataset /Users/xuejian/Desktop/labelme/json/%d.json -o /Users/xuejian/Desktop/labelme/data/%d_json' % (i, i))

# dst_w=512
# dst_h=512
# dst_shape=(dst_w,dst_h,3)
train_image = path+'image/'
if not os.path.exists(train_image):
    os.makedirs(train_image)
train_label = path+'label/'
if not os.path.exists(train_label):
    os.makedirs(train_label)

for i in range(n):
    print(i)
    img = cv2.imread(path+'data/%d_json/img.png' % i)
    label = cv2.imread(path+'data/%d_json/label.png' % i)
    print(img.shape)
    label = label / np.max(label[:, :, 2]) * 255
    label[:, :, 0] = label[:, :, 1] = label[:, :, 2]
    print(np.max(label[:, :, 2]))
    # cv2.imshow('l',label)
    # cv2.waitKey(0)
    print(set(label.ravel()))
    cv2.imwrite(train_image + '%d.png' % i, img)
    cv2.imwrite(train_label + '%d.png' % i, label)