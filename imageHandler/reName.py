from PIL import Image
import os
from PIL import Image

now_path = '/Users/xuejian/Desktop/baiduResult'
new_dir = '/Users/xuejian/Desktop/license/'
# 修改图片大小
def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)
index = 0
for file_name in os.listdir(now_path):
    if ('DS_Store' not in file_name):
        if('_' in file_name):
            file_out = file_name.split('.')[0].split('_')[1]+'.png'
        else:
            file_out = file_name.split('.')[0]+'.png'
        files_path = now_path + '/' + file_name
        produceImage(files_path, 512, 512, new_dir+file_out)

