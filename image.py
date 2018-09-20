# coding:utf-8
#所有最长边大于800的图片，不改变比例处理成最大边800像素
"""
Author: goldfilm2all@gmail.com
Version: 1.0
"""

from __future__ import division
import os
import sys
import Image

def main(args=None):
	USAGE = "Usage:	python *.py [folder]"
	print "start..."
	if args == None:
		args = sys.argv[1:]
		args.append(os.getcwd())		#或者指定当前目录
	if not args or not os.path.isdir(args[0]):
		print USAGE
		sys.exit(1)

	for root, dir, filenames in os.walk(args[0]):
		#print root, dir, filenames
		if filenames:
			for filename in filenames:
				if not os.path.splitext(filename)[1].upper() in format:
					pass
				else:
					print filename
					resize(root.replace("\\","/")+"/"+filename)

def resize(filename):
	#(fileName,fileEx) = os.path.splitext(os.path.basename(filename))
	img = Image.open(filename)
	size = img.size
	#print size
	max_pixel =  max(size[0],size[1])
	if max_pixel > 1280:
		radio = size[0]/size[1]
		if size[0] == max_pixel:
			l_pixel = 1280
			w_pixel = int(l_pixel*(1/radio))
		else:
			w_pixel = 1280
			l_pixel = int(w_pixel*radio)
		#print radio,l_pixel,w_pixel
		new_img = img.resize((l_pixel,w_pixel),Image.BILINEAR)
		new_img.save(filename)
		print "resize "+filename+"		(%s,%s) --> (%s,%s)" % (size[0],size[1],l_pixel,w_pixel)
	else:
		pass

if __name__ == "__main__":
	format = [".JPG",".BMP"]
	main()
	print "done"
