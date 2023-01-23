import os
import twitter
#This imports the twitter library for it to run
from PIL import Image, ImageDraw, ImageFont
#import numpy
#import scipy
#import matplotlib
#These Import numpy, scipy, and matplotlib as well for use of their items

#from words import *
#from gtts import gTTS

from time import sleep
#times will allow for use of setting a time between the tweets

sortedmessages = []
justmessages = []
searchlist = []
completedposts = [["Y’all \U0001f921 stuck on thinking somebody tryna hate y’all and I’m just tryna \U0001f4a9 properly. [REDACTED]", None],["Man 2 things you can neva come back from is being \U0001f1f4a3 & Being A \U0001f984", None],["Either no one wants a \U0001f984, or you’re too \U0001f60E     . That’s the new definition of asexuality", None]]
#these setup blank lists to be used by the functions

from credentials import *
#loads credentisl from file
#better privacy, and security

from emoji import*
#this imports the emoji dictionary that is a major pain in the ass to assemble.

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret, tweet_mode='extended')

#This is the authentication for twitter. My keys have been removed
#where ever it says "FILL HERE" place your coresponding twitter key.

def posttweet(lis):
	#""""
	#Posts a tweet to twitter. Takes a string.
	#""""
	return api.PostUpdate(lis[0], media=lis[1])

#def postvideo(text,video):
#	response = tweeter.upload_video(media=video, media_type='video/mp4')
#	tweeter.update_status(status=text, media_ids=[response['media_id']])

	
def postmessage(mes,use_id=None,scr_name=None):
	"""
	Can post a message the specified twitter user
	"""
	return api.PostDirectMessage(mes,use_id,scr_name)
	

def search(thin):
	del searchlist[:]
	temp = searchbreakdown(api.GetSearch(thin))
	
	
def searchbreakdown(lis):
	"""
	This takes the direct messages information and sorts it into readable format
	It also saves it into a csv file for late reference.
	"""
	
	count = 0
	splitcount = 0
	deletecount = 0
	
	while (count < len(lis)):
		temp = repr(lis[count])
		lis[count] = temp[7:len(temp)-1]
		count = count+1
	#This seperates the usless parts off the info (status)	
		
	while splitcount < len(lis):
		lis2 = lis[splitcount]
		if lis2[len(lis2)-1]=="'":
			lis[splitcount] = lis2.split("'", 1)
			lis[splitcount] = lis[splitcount][1]
			lis[splitcount] = lis[splitcount][:len(lis[splitcount])-1]
		else:
			lis[splitcount] = lis2.split('"', 1)
			lis[splitcount] = lis[splitcount][1]
			lis[splitcount] = lis[splitcount][:len(lis[splitcount])-1]
		splitcount = splitcount+1
		
	#This takes the one chunck and splits it into individual parts	
	#it also removes the uneeded first part that contained
	#the time, date, user information.
	#it also removes the last character, ' or " which was
	#used to determine which one to split on.

def justmessage():
	del justmessages[:]
	for items in sortedmessages:
		temp = len(items[1][1])-2
		justmessages.append(items[1][1][2:temp])
		
		
def getmessage():
	mes = api.GetDirectMessages()
	dirmesagesortandfile(mes) 

def deletemesages():
	count = 0
	while count<len(sortedmessages):
		api.DestroyDirectMessage(sortedmessages[count][0][1])
		count  = count + 1
		
	
def sortedmessage(lis):
	tempsort = (dirmesagesortandfile(lis))
	savefi(sortedmessages)
	return sortedmessages
	
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
	
	
	#messagelist = []
	#print (messagelist)
	innerlist = []
	
	#needed fields for following section
	#count2 = 0
	for lis2 in lis:
			tempid = lis2[0]
			id = tempid.split('=')
			innerlist.append(id)
			#Takes the ID section splits it into a list then adds it into messagelist
		
	
			#tempsender = lis2[1]
			#sender = tempsender.split('=')
			#innerlist.append(sender)
			#same as above, but with sender
		
	
			#tempcreated = lis2[2]
			#created = tempcreated.split('=')
			#innerlist.append(created)
			#same as above, but with created
		
	
			temptext = lis2[3]
			text = temptext.split('=')
			innerlist.append(text)
			#same as above, but with message
		
	
			#messagelist.append(innerlist)
			sortedmessages.append(innerlist)
			print (innerlist)
			innerlist = []
		
				#count2 = count2+1
	#deletemesages()
	#savefi(messagelist)
	#lis = messagelist
	#return lis
	#lis = messagelist
	#print (messagelist)
	

	
	#this takes the individual pieces format: Title=Info
	#splits it on the '=' and adds them to a list that
	#contains the other information for that message
	#Then adds it to one list of all the messages

def completeposts(lis):
	savevideo(lis)
	count = 0
	while count < len(lis):
		completedposts.append([sortedmessages[count][1],str(count)+'.mp4'])
		count = count + 1

#if len(sortedmessages)<5:
#	sortedmessages.append(search(term))

#pausetime= (1000//len(completedposts)
def aaaaa(lis):
	pausetime= (1000//len(lis))
	count = len(lis)
	while count != 0:
		posttweet(lis[0])
		del lis[0]
		count = count - 1
		sleep(pausetime)
	
#""""
#def savefi(lis):
#	with open('messagelist.csv', 'w', newline='') as csvfile:
#		writer = csv.writer(csvfile)
#		writer.writerows(lis)
#	#This writes complete list as a csv file.
#	
3	#return lis
#""""

#def savefi():
#	with open('messagelist.txt', 'w') as fp:
#		for item in :c
#			fp.write("{}\n".format(item))
	#This writes complete list as a csv file.
	
	#return lis

def savemp3(lis):
	count = 0
	count2 = 0
	while count < len(lis):
		tts = gTTS(text=lis[count2], lang='en-uk')
		tts.save(str(count2)+'.mp3')
		count = count+1
		count2 = count2+1

def saveimage(lis):
	count = 0
	while count < len(lis):
		image = Image.open('background.png')
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('Roboto-Black.ttf', size = 50)
		(x, y) = (50, 60)
		colour = 'rgb(0,0,0)'
		if len(lis[count]) > 40:
			character = ' '
			searchnumber = 40
			indexlist = [pos for pos, char in enumerate(lis[count]) if char == character]
			myarray = np.array(indexlist)
			pos = (np.abs(myarray-searchnumber)).argmin()
			line1 = lis[count][:pos]
			draw.text((x, y), line1, fill=colour, font=font)
			if len(lis[count][pos+1:]) > 40:
				searchnumber2 = searchnumber+40
				pos2 = (np.abs(myarray-searchnumber2)).argmin()
				line2 = len(lis[count][pos+1:pos2])
				(x, y) = (50, 182)
				draw.text((x, y), line2, fill=colour, font=font)
				if len(lis[count][pos2+1:]) > 40:
					searchnumber3 = searchnumber2 +40
					pos3 = (np.abs(myarray-searchnumber3)).argmin()
					line3 = lis[count][pos2+1:pos3]
					(x, y) = (50, 284)
					draw.text((x, y), line3, fill=colour, font=font)
					if len(lis[count][pos3+1:]) > 40:
						searchnumber4 = searchnumber3 +40
						pos4 = (np.abs(myarray-searchnumber4)).argmin()
						line4 = lis[count][pos3+1:pos4]
						(x, y) = (50, 388)
						draw.text((x, y), line4, fill=colour, font=font)
						if len(lis[count][pos4+1:]) > 40:
							searchnumber4 = searchnumber4 +40
							pos5 = (np.abs(myarray-searchnumber5)).argmin()
							line5 = lis[count][pos4+1:pos5]
							(x, y) = (50, 388)
							draw.text((x, y), line5, fill=colour, font=font)
							if len(lis[count][pos5+1:])<=40:
								(x, y) = (50, 590)
								line6 = lis[count][pos5+1:]
								draw.text((x, y), line6, fill=colour, font=font)
								image.save(str(count)+'.jpeg')
								count = count +1
							else:
								image.save(str(count)+'.jpeg')
								count = count +1
						else:
							image.save(str(count)+'.jpeg')
							count = count +1
					else:
						image.save(str(count)+'.jpeg')
						count = count +1
				else:
					image.save(str(count)+'.jpeg')
					count = count +1
			else:
				image.save(str(count)+'.jpeg')
				count = count +1
		else:
			draw.text((x, y), lis[count], fill=colour, font=font)
			image.save(str(count)+'.jpeg')
			count = count +1

def word(lis):
	finlis = []
	for each in lis:
		print(each)
		sleep(1)
		holdlist = []
		for item in each:
			print(item)
			sleep(1)
			for word in wordselim:
				print(word)
				sleep(1)
				if item == word:
					holdlist.append('changed')	
			
			holdlist.append(item)
		finlis.append(holdlist)	
	return finlis
	
def savevideo(lis):
	count = 0
	while count < len(lis):
		#a = "ffmpeg -loop 1 -y -i"+ "+str(count)+".mp3"+" -shortest "+str(count)+".mp4"
		#os.system(a)
		count = count +1
