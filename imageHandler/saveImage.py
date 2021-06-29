import urllib
# -*- coding: utf-8 -*-

import urllib.request
import xlrd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

filename = "/Users/xuejian/Desktop/result1.xls"

book = xlrd.open_workbook(filename)  # 打开一个工作薄，不需要手动进行关闭

sheet = book.sheet_by_index(0)  # 获取一个工作表，以index的方式，这里是获取第1个工作表


print(sheet.nrows)
print(sheet.ncols)
index = 0
for i in range(0, sheet.nrows):
    for j in range(0, sheet.ncols):
        print(sheet.cell_value(i, j))  # 打印单元格[i,j]的值
        img_src = sheet.cell_value(i, j).split('--')[1]
        img_name = sheet.cell_value(i, j).split('--')[0]
        urllib.request.urlretrieve(img_src,'/Users/xuejian/Desktop/crm/'+str(index)+'_'+img_name+'.jpg')
        index = index +1



print(sheet.row_values(0))  # 打印工作表第一行的值



# 网络上图片的地址
#img_src = sheet.row_values(0).split('-')【】

# 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
#urllib.urlretrieve(img_src,'')
