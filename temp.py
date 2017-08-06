def get_temp():
	#encoding:utf-8
	#decoding:utf-8
	#codion:utf-8

	import urllib
	import urllib.request
	import bs4
	import re

	rssurl = "http://weather.livedoor.com/forecast/rss/area/160010.xml"

	tenki = 0
	temp = 0

	with urllib.request.urlopen(rssurl) as res:
		xml = res.read()
		soup = bs4.BeautifulSoup(xml,"html.parser")
		for item in soup.find_all("item"):
			title = item.find("title").string
			if title.find("[ PR ]") == -1:
				tenki = title
				#tenki.append(title)
				break

	for i in range(50) :
		if tenki[i] == '℃':
			temp = int(tenki[i-1])
			temp += int(tenki[i-2])*10
			break
	#print (temp)
	return temp