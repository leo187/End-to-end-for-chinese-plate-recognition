import flask
from flask import request
import urllib.request
import time
import ssl
import cv2
import numpy as np
from tensorflow import keras
from core import locate_and_correct
from Unet import unet_predict
from CNN import cnn_predict
import os



def test():
    test_path = '/Users/xuejian/Desktop/源数据/TEST-PIC/'  # 利用百度API标注或手动标注好的图片
    listdir = os.listdir(test_path)
    # print(listdir)
    index = 0
    arr = []
    for name in listdir:
        if ('DS_Store' not in name):
            print('数量'+str(index) )
            result = display(test_path + name, 'unet.h5', 'cnn.h5', 8)
            index = index+1
            if(result.replace('·','') != name.split('.')[0].split('_')[1]) :
                arr.append(name+'---'+result.replace('·',''))
    print('********************************************')
    print('失败数量' + str(len(arr)))
    print(str(arr))


def display(img_src_path,unetModel,cnnModel,picSize):
    unet = keras.models.load_model(unetModel)
    cnn = keras.models.load_model(cnnModel)
    img_src = cv2.imdecode(np.fromfile(img_src_path, dtype=np.uint8), -1)  # 从中文路径读取时用
    h, w = img_src.shape[0], img_src.shape[1]
    if h * w <= 240 * 80 and 2 <= w / h <= 5:  # 满足该条件说明可能整个图片就是一张车牌,无需定位,直接识别即可
        lic = cv2.resize(img_src, dsize=(240, 80), interpolation=cv2.INTER_AREA)[:, :, :3]  # 直接resize为(240,80)
        img_src_copy, Lic_img = img_src, [lic]
    else:  # 否则就需通过unet对img_src原图预测,得到img_mask,实现车牌定位,然后进行识别
        img_src, img_mask = unet_predict(unet, img_src_path)
        img_src_copy, Lic_img = locate_and_correct(img_src, img_mask)  # 利用core.py中的locate_and_correct函数进行车牌定位和矫正

    Lic_pred = cnn_predict(cnn, Lic_img)  # 利用cnn进行车牌的识别预测,Lic_pred中存的是元祖(车牌图片,识别结果)
    result = 'fail'
    if Lic_pred:
        print(Lic_pred[0][1])
        result = Lic_pred[0][1]
    return result

test()