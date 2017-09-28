"""
	Code written by Tu Thanh Nguyen
	Date : September 17, 2017 
	Last Update: September 18, 2017
"""

from PIL import Image
import os
import os.path
import re

SIZES = 100, 100
class ScaleImage:
	def __init__(self,path):
		self.path=path
	def readFile(self):
		return [x for x in os.listdir(self.path) if re.match('.*\.[gif|png|jpeg|jpg|png|JPG]', x)]
	def readImage(self,im):
		return Image.open(self.path+im).convert('RGB')
	def resizeImage(self,img):
		return img.resize(SIZES,Image.ANTIALIAS)
	def saveImage(self,path,img):
			img.save(path,quality=195)
