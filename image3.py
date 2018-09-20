#把三个图片纵向合并
import sys
#导入sys模块
from PIL import Image
#从PIL导入Image模块
images = map(Image.open, ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg'])
#map()会把Image.open 应用到后面list的每个item 并把返回的map对象复制给images
#widths, heights = zip(*(i.size for i in images))

total_width = 880
max_height = 10120

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (0, x_offset))
    x_offset += im.size[1]

new_im.save('test.jpg')
