def generation():
	import cv2 as cv
	import numpy as np
	import copy

	img1 = cv.imread("zentai_2.jpg")
	rows,cols,channels = img1.shape


	img2 = img1[rows//3:(rows*7//15), 0:cols ]

	kernel = np.ones((6,6),np.float32)/36
	img2 = cv.filter2D(img2,-1,kernel)
	img2 = cv.flip(img2,0)

	img3 = copy.deepcopy(img1)
	img3[rows//3:(rows*7//15), 0:cols ] = img2
	img3 = cv.addWeighted(img1,0.5,img3,0.5,2,2)

	cv.imshow('add after2',img3)
	#cv.imwrite("out.jpg",img3)
