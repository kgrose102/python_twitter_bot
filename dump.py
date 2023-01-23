from PIL import Image, ImageDraw, ImageFont

image = Image.open('background.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Black.ttf', size = 50)
(x, y) = (50, 80)
colour = 'rgb(0,0,0)'
draw.text((x, y), l1, fill=colour, font=font)
image.save('testlen.jpeg')

ffmpeg -r 1 -loop -i test.png -i 2.mp3 -acodec copy -r 1 -shortest -vf scale=720:480 test.mp4

ffmpeg -loop 1 -y -i test.png -i 2.mp3 -shortest test.mp4

ffmpeg -i test.png -i 2.mp3 -acodec copy -r 1 -shortest test.mp4

ffmpeg -loop 1 -y -i test.jpeg -i 0.mp3 -shortest test12.mp4

image = Image.open('background.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Black.ttf', size = 50)
(x, y) = (50, 60)
colour = 'rgb(0,0,0)'
if len(lis[count]) > 40:
	c = ' '
	searchnumber = 40
	indexlist = [pos for pos, char in enumerate(lis[count]) if char == c]
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
					if len(lis[count][pos5+1:])=<20
						(x, y) = (50, 590)
						line6 = lis[count][pos5+1:]
						draw.text((x, y), line6, fill=colour, font=font)
						image.save(str(count)+'.jpeg')
					else:
						image.save(str(count)+'.jpeg')
				else:
					image.save(str(count)+'.jpeg')
			else:
				image.save(str(count)+'.jpeg')
		else:
			image.save(str(count)+'.jpeg')
	else:
		image.save(str(count)+'.jpeg')
else:
	draw.text((x, y), lis[count], fill=colour, font=font)
	image.save(str(count)+'.jpeg')