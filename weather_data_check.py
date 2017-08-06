def check(mon,ho,tmp,ws,wv):
	# -*- coding: utf-8 -*-
	import urllib.request
	import bs4

	flag = 0

	month = mon
	hour = ho
	temp = tmp
	wind_s = ws
	wind_v = wv

	if( 3 <= month <= 5):
		flag+=1
	if( 11 <= hour <= 16):
		flag+=1
	if( 18 <= temp):
		flag+=1
	if( wind_s <= 3):
		flag+=1
	if( wind_v == "北北東"):
		flag+=1

	return int(flag)