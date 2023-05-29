import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random

random.seed()

#create directory on exist, otherwise do nothing
#checks if Histograms folder exists before making one to store histogram files
#https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
def dirExist(pathDir):
	if not os.path.exists(pathDir):
		os.makedirs(pathDir)

#checks every country in qualified list
#takes data from dataArr, makes np.array
#sends to histogram generator in matplotlib
#extra visual stuff to make it look pretty
def indivHist(qualCountryList, dataArr):
	#have to include a very tiny amount above the int we want so that the bin is [1,5.01)
	#which includes the 5 rank, very important for accurate analysis while still looking good
	binEdge = [1,5.01,10.01,15.01,20.01,26]
	
	dirExist('Individual_Histograms')

	for country in qualCountryList:
		#access array from dataArr['country']
		rank = np.array(dataArr[country])
		#https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
		#https://stackoverflow.com/questions/13714454/specifying-and-saving-a-figure-with-exact-size-in-pixels
		plt.figure(figsize=(2560/300, 1440/300), dpi=300)
		#https://medium.com/@arseniytyurin/how-to-make-your-histogram-shine-69e432be39ca
		#we add patches for custom colors on each bin
		rank, bins, patches = plt.hist(rank, binEdge, edgecolor='#101010',linewidth=.5)
		#color grading for each bin
		patches[0].set_facecolor('#49b249')
		patches[1].set_facecolor('#9cdc38')
		patches[2].set_facecolor('#e7e728')
		patches[3].set_facecolor('#d7a838')
		patches[4].set_facecolor('#b94949')
		plt.xlim(1, 26)
		plt.xticks([1,5,10,15,20,26])
		plt.yticks(np.arange(0, 22, step=2))
		#sweden breaks the chart because it's sweden
		if country == 'sweden':
			plt.yticks(np.arange(0,33,step=2))
		plt.xlabel('Rank given by other countries')
		plt.ylabel('Count')
		plt.title(country + ' jury rank')
		width = patches[0].get_width() + patches[1].get_width()+random.uniform(-1.5, 2)
		height = patches[2].get_height()+random.uniform(3,6.5)
		plt.text(width, height, 'Reddit: u/WhenAmINotStruggling', fontsize=5, alpha=.5)
		plt.text(width, height-.5, 'Github: JeremyBallard', fontsize=5, alpha=.5)
		plt.savefig('Individual_Histograms/' + country + 'JuryRanksGiven.png')
		#defining custom figure resolution means using this not plt.clf()
		plt.close()

#country is a string of the country you want
#generates top 3 of any country passed in
#generates 1st 2nd 3rd regardless of a country getting any of that rank
def top3Hist(country, dataArr):
	dirExist('HistogramTop3')
	binEdge = [0.5, 1.5, 2.5, 3.5]
	rank = np.array(dataArr[country])
	plt.figure(figsize=(2560/300, 1440/300), dpi=300)
	rank, bins, patches = plt.hist(rank, binEdge, edgecolor='#101010',linewidth=.5)
	plt.xlim(0.5,3.5)
	#https://stackoverflow.com/questions/12998430/how-to-remove-xticks-from-a-plot
	plt.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
	plt.yticks(np.arange(0,20,step=2))
	plt.title(country + ' jury rank top 3')
	patches[0].set_facecolor('#44ac44')
	patches[1].set_facecolor('#72c243')
	patches[2].set_facecolor('#9cdc38')
	#https://stackoverflow.com/questions/32785705/how-to-label-patch-in-matplotlib
	#get_height + 1 makes it look prettier
	plt.text(patches[0].get_width(), patches[0].get_height()+1, '1st')
	#add first width to second width for correct alignment
	plt.text(patches[0].get_width() + patches[1].get_width(), patches[1].get_height()+1, '2nd')
	plt.text(patches[0].get_width() + patches[1].get_width() + patches[2].get_width(), patches[2].get_height()+1, '3rd')
	width = patches[0].get_width() + patches[1].get_width()+random.uniform(-.5,.5)
	height = patches[1].get_height()+random.uniform(3,6.5)
	plt.text(width, height, 'Reddit: u/WhenAmINotStruggling', fontsize=5, alpha=.5)
	plt.text(width, height-.5, 'Github: JeremyBallard', fontsize=5, alpha=.5)
	plt.savefig('HistogramTop3/' + country +'Top3.png')
	plt.close()

def matchupHist(countryHead, dataArr, colors=None):
	if len(countryHead) != 2 and type(countryHead) is not list:
		print('Need exactly two countries in a list to make head to head work')
		return
	dirExist('1v1Histogram')
	#binEdge line to plt.ylabel line can be its own function
	#need to pass figure in and out of it though
	binEdge = [1,5.01,10.01,15.01,20.01,26] 
	
	rank = []
	#makes an array of arrays, which allows hist to generate side by side bars
	for country in countryHead:
		rank.append(np.array(dataArr[country]))
	plt.figure(figsize=(2560/300, 1440/300), dpi=300)
	#https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html
	#https://matplotlib.org/stable/gallery/color/named_colors.html
	#color and label can have arrays passed into them
	#label[0]=colors[0]
	#rwidth is a multiplier to the bars so they fill out the xticks
	rank, bins, patches = plt.hist(rank, binEdge, color=colors, label=countryHead, rwidth=1)
	plt.xlim(1,26)
	plt.xticks([1,5,10,15,20,26])
	plt.xlabel('Rank given by other countries')
	plt.ylabel('Count')
	plt.title(countryHead[0] + ' vs. ' + countryHead[1] + ": Ranks by Jury")
	plt.legend(prop={'size': '14'})
	width = 10+random.uniform(-1.5, 2)
	height = 12+random.uniform(1,2.5)
	plt.text(width, height, 'Reddit: u/WhenAmINotStruggling', fontsize=5, alpha=.5)
	plt.text(width, height-1, 'Github: JeremyBallard', fontsize=5, alpha=.5)
	plt.savefig('1v1Histogram/' + countryHead[0]+countryHead[1]+'Matchup.png')
	plt.close()

def traitHist(countryHead, dataArr, title, colors=None):
	dirExist('TraitHistogram')
	binEdge = [1,5.01,10.01,15.01,20.01,26] 
	rank = []
	#makes an array of arrays, which allows hist to generate side by side bars
	for country in countryHead:
		rank.append(np.array(dataArr[country]))
	plt.figure(figsize=(2560/300, 1440/300), dpi=300)
	rank, bins, patches = plt.hist(rank, binEdge, color=colors, label=countryHead, rwidth=1, histtype='barstacked')
	plt.xlim(1,26)
	plt.xticks([1,5,10,15,20,26])
	plt.xlabel('Rank given by other countries')
	plt.ylabel('Count')
	plt.title(title)
	plt.legend()
	height = 0
	#grab height for stacked bars
	for bars in range(len(patches)):
		height += patches[bars][1].get_height()
	height += random.uniform(4,8.5)
	width = 6+random.uniform(-1.5, 2)
	plt.text(width, height, 'Reddit: u/WhenAmINotStruggling', fontsize=5, alpha=.5)
	plt.text(width, height-2, 'Github: JeremyBallard', fontsize=5, alpha=.5)
	plt.savefig('TraitHistogram/' + title + '.png')
	plt.close()

qualCountryList = ['albania', 'armenia', 'australia', 'austria', 'belgium', 'croatia',
'cyprus','czechia','estonia','finland','france','germany','israel','italy','lithuania',
'moldova','norway','poland','portugal','serbia','slovenia','spain','sweden','switzerland',
'ukraine','united-kingdom']

countryList = ['albania', 'armenia', 'australia', 'austria', 'azerbaijan', 'belgium', 
'croatia', 'cyprus', 'czechia', 'denmark', 'estonia', 'finland', 'france', 'georgia', 
'germany', 'greece', 'iceland', 'ireland', 'israel', 'italy', 'latvia', 'lithuania',
'malta', 'moldova', 'netherlands', 'norway', 'poland', 'portugal', 'romania', 
'san-marino', 'serbia', 'slovenia', 'spain', 'sweden', 'switzerland', 'ukraine',
'united-kingdom']

dataArr = {country:[] for country in qualCountryList}
pdJuryData = pd.read_csv('juryRank.csv', index_col = 0).astype(pd.Int64Dtype())
tempArr = []
for row in pdJuryData.itertuples(name='Country'):
	#get Country name, use for storing later at arr index
	qualCountry = getattr(row, 'Index')
	for country in countryList:
		#for some reason pandas dataframe refuses to get our poor children san marino or united kingdom
		#so we need to do some extra adjustments to make it work properly
		#countryStr is what we use to find where to put our row data into dataArr
		#country is the actual dataframe column name
		countryStr = qualCountry
		if country == 'san-marino':
			country = '_30'
		elif country == 'united-kingdom':
			country = '_37'
			countryStr = 'united-kingdom'

		#grab each jury's rank and add them to the temp list
		tempArr.append(getattr(row, country))
	#put the values from row into array at that string
	for i in range(len(tempArr)):
		dataArr[qualCountry].append(tempArr[i])
	tempArr.clear()

#Histogram processing for specific things
#Each function will come with a comment describing the function, and then the function
#Uncomment the function to run that function

#Makes figures for each country, grouped in bins: 1-5, 6-10, 11-15, 16-20, 21-26
#indivHist(qualCountryList, dataArr)

#Top 3 jury ranks for the top 4 by jury countries
#top3Hist('sweden', dataArr)
#top3Hist('italy', dataArr)
#top3Hist('israel', dataArr)
#top3Hist('finland', dataArr)

#1v1 Matchups based on jury Rank
#matchupHist(['sweden','finland'], dataArr, ['gold', '#32cd32'])
#matchupHist(['italy', 'israel'], dataArr, ['#43b043', 'royalblue'])

#Trait matchups for various groupings like jury darlings, jury darlings but flops, out of the box, etc
#traitHist(['sweden', 'estonia', 'italy'], dataArr, 'jury darlings', ['gold', 'skyblue', '#43b043'])
#traitHist(['france', 'spain', 'switzerland'], dataArr, 'jury darlings but flops', ['midnightblue', 'goldenrod',  'red'])
#traitHist(['croatia', 'serbia', 'finland', 'ukraine', 'germany'], dataArr, 'unique songs', 
	#['blue', '#C7363D', '#32cd32', '#0057B7', 'firebrick'])
#traitHist(['croatia', 'slovenia', 'germany', 'australia'], dataArr, 'rock metal bands', ['blue', '#fc8eac','maroon', '#E4002B'])
#traitHist(['albania', 'moldova', 'portugal', 'czechia'], dataArr, 'ethnic songs', ['maroon', '#ffd100', '#e42518', '#11457E'])