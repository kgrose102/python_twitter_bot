
import twitter
import numpy
import scipy
import matplotlib
#This imports the twitter library for it to run
#Imports numpy, scipy, and matplotlib as well for use of their items
import csv
from time import sleep
#times will allow for use of setting a time between the tweets

from credentials import *
#loads credentisl from file
#better privacy, and security

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret, tweet_mode='extended')
#This is the authentication for twitter. My keys have been removed
#where ever it says "FILL HERE" place your coresponding twitter key.

def posttweet(phrase):
	return api.PostUpdate(phrase)
	
def postmessage(mes,use_id=None,scr_name=None):
	return api.PostDirectMessage(mes,use_id,scr_name)

def getmessage():
	mes = api.GetDirectMessages()
	dirmesagesortandfile(mes) 
		

def dirmesagesortandfile(lis):
	"""
	This takes the direct messages information and sorts it into readable format
	It also saves it into a csv file for late reference.
	"""
	
	count = 0
	splitcount = 0
	
	while (count < len(lis)):
		temp = repr(lis[count])
		lis[count] = temp[14:len(temp)-1]
		count = count+1
	
	#This seperates the usless parts off the info (directmessage)	
		
	while splitcount < len(lis):
		lis2 = lis[splitcount]
		lis[splitcount] = lis2.split(', ')
		splitcount = splitcount+1
	
	#This takes the one chunck and splits it into individual parts	
	
	
	messagelist = []
	print (messagelist)
	innerlist = []
	
	#needed fields for following section
	#count2 = 0
	for lis2 in lis:
			tempid = lis2[0]
			id = tempid.split('=')
			innerlist.append(id)
			#Takes the ID section splits it into a list then adds it into messagelist
		
	
			tempsender = lis2[1]
			sender = tempsender.split('=')
			innerlist.append(sender)
			#same as above, but with sender
		
	
			tempcreated = lis2[2]
			created = tempcreated.split('=')
			innerlist.append(created)
			#same as above, but with created
		
	
			temptext = lis2[3]
			text = temptext.split('=')
			innerlist.append(text)
			#same as above, but with message
		
	
			messagelist.append(innerlist)
			print (innerlist)
			innerlist = []
		
				#count2 = count2+1
	savefi(messagelist)
	#lis = messagelist
	#print (messagelist)
	
	
	#this takes the individual pieces format: Title=Info
	#splits it on the '=' and adds them to a list that
	#contains the other information for that message
	#Then adds it to one list of all the messages
""""
def savefi(lis):
	with open('messagelist.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(lis)
	#This writes complete list as a csv file.
	
	#return lis
""""

def savefi(lis):
	with open('messagelist.txt', 'w') as fp:
		for item in lis:
			fp.write("{}\n".format(item))
	#This writes complete list as a csv file.
	
	#return lis