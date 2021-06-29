from PIL import Image
import os
from PIL import Image

now_path = '/Users/xuejian/Desktop/unet/'
new_dir = '/Users/xuejian/Desktop/unetRename/'
# 修改图片大小

index = 0
for file_name in os.listdir(now_path):
    if ('DS_Store' not in file_name):
        try:
            os.rename(now_path+file_name, new_dir+str(index)+'.jpg')
            index = index+1
        except Exception as e:
            print(e)
            print('rename file fail\r\n')
        else:
            print('rename file success\r\n')



