import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
#access array from dataArr['country']
binEdge = [1,5,10,15,20,26]
#fix later
for country in qualCountryList:
	rank = np.array(dataArr[country])
	#https://medium.com/@arseniytyurin/how-to-make-your-histogram-shine-69e432be39ca
	plt.hist(rank, binEdge, edgecolor='#101010',linewidth=.5)
	plt.xlim(1, 26)
	plt.yticks(np.arange(0, 22, step=2))
	plt.xlabel('Rank given')
	plt.title(country + ' jury rank')
	plt.show()