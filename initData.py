from PreProcessing.ScaleImage  import ScaleImage
import os
import os.path

PATH = 'Data-Raw/'
TRAIN = 'Train/'
TEST = 'Test/'
Labels = os.listdir(PATH)
for label in Labels:
	print "PreProcessing Label:", label 
	im = ScaleImage(PATH+label+'/')
	files = im.readFile()
	index=2
	if len(files) > 0:
		for file in files:
			print "Processing file ", file 
			img = im.readImage(file)
			img = im.resizeImage(img)
			if index % 2 == 0 :
				im.saveImage(TRAIN + label + '/' + str(index/2)+'.jpg',img)
			else: 
				im.saveImage(TEST + label + '/' + str(index/2) + '.jpg',img)
			index = index + 1
