#!/usr/bin/env python
# -*- coding : utf-8 -*-


entry="Regular: 16Mar2009(    mon), 17Mar2009(tues), 18Mar2009(wed)"
#Dictionary
hotels={
	'Lakewood':{
		'rating':3,
		'weekday':{
			'regular':110,
			'reward':80,
			},
		'weekend':{
			'regular':90,
			'reward':80,
			},
		},
	'Bridgewood':{
		'rating':4,
		'weekday':{
			'regular':160,
			'reward':110,
			},
		'weekend':{
			'regular':60,
			'reward':50,
			},
		},
	'Ridgewood':{
		'rating':5,
		'weekday':{
			'regular':220,
			'reward':100,
			},
		'weekend':{
			'regular':150,
			'reward':40,
			},
		},
	}
#end Dictionary
#print hotels.keys()#name of hotels
#print hotels.values()#values for each hotel 
#print hotels.items()#don't understand at all 
#get necessary info
#print ""
#print ""

obtain=[]
prefer=[]

def get_info(obtain):
	#for to manage necessary data on array
	for val in hotels.values():
		obtain.append(val)
	#endfor
#end fun
def pretify(entry):
	entry = entry.replace(" ","")
	entry = entry.replace(":",",")
#end fun



get_info(obtain)#select data
pretify(entry)#pretify input user





