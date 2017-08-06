#encoding:utf-8
#decoding:utf-8
#codion:utf-8

import cv2 as cv
import numpy as np
import fake_mirage_generation as fake_mirage
import weather_data_check as weather_data
import temp

if weather_data.check(1,10,temp.get_temp(),4,"南") <= 3:
	fake_mirage.generation()

keycode = cv.waitKey(0)

if keycode == ord("p"):
	
	cv.destroyAllwindows()