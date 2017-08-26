#!/usr/bin/env python

#BING wallpaper for Desktop

#BEFORE RUNNING THIS FILE GIVE IT PERMISSION TO EXECUTE!!!

import os,re,urllib
import xml.etree.ElementTree as ET

url="https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en_US"
#url of bing photo of the day
#here format is xml and idx=0 means today if it is 1 then it is for yesterday
#n=1 is for number of images previous the day given by idx and mkt is Bing market area

try:
	page=urllib.urlopen(url)
	#open the url

	xml=ET.parse(page).getroot()
	#get all the contents(elements) of xml page

	images=xml.findall("image")
	#find all the images tags in it and make a list to contain them

	base_image=images[0].find("url").text
	#image with resolution 1366x768 to convert in better quality we convert it into 1920x1080

	correct_image=re.sub(r'\d+x\d+', "1920x1080", base_image)
	#replaced 1366x768 with 1920x1080

	image_url="https://www.bing.com" + correct_image

	image_name=images[0].find("startdate").text+".jpg"


	file_path="/root/Pictures/bing_xml/"

	def create_path(c):
		if os.path.exists(c) is False:
			os.makedirs(c)		

	create_path(file_path)				
	image_path=file_path+image_name


	if os.path.exists(image_path) is False:
		urllib.urlretrieve(image_url,image_path)
		command = 'gsettings set org.gnome.desktop.background picture-uri file://'+image_path
		os.system(command)
		notify = 'notify-send -u critical "Wallpaper updated successfully"'
		os.system(notify)

	else:
		notify= 'notify-send -u critical "Wallpaper has been already updated!"'
		os.system(notify)

except:
	notify='notify-send -u critical "Wallpaper cannot be updated! \n Error occur!"'
	os.system(notify)
