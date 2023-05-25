import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

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

binEdge = [1,5,10,15,20,26]
#checks if Histograms folder exists before making one to store histogram files
#https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
if not os.path.exists('Histograms'):
	os.makedirs('Histograms')
#checks every country in qualified list
#takes data from dataArr, makes np.array
#sends to histogram generator in matplotlib
#extra visual stuff to make it look pretty
for country in qualCountryList:
	#access array from dataArr['country']
	rank = np.array(dataArr[country])
	#https://medium.com/@arseniytyurin/how-to-make-your-histogram-shine-69e432be39ca
	plt.hist(rank, binEdge, edgecolor='#101010',linewidth=.5)
	plt.xlim(1, 26)
	plt.yticks(np.arange(0, 22, step=2))
	#germany breaks the chart cause of all the lasts
	if country == 'germany':
		plt.yticks(np.arange(0,26,step=2))
	#sweden breaks the chart because it's sweden
	if country == 'sweden':
		plt.yticks(np.arange(0,30,step=2))
	plt.xlabel('Rank given by other countries')
	plt.ylabel('Count')
	plt.title(country + ' jury rank')
	plt.savefig('Histograms/' + country + 'JuryRanksGiven.png')
	plt.clf()