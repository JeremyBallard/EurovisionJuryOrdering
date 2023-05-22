import pandas as pd
import numpy as np
import matplotlib as mpl

qualCountryList = ['albania', 'armenia', 'australia', 'austria', 'belgium', 'croatia',
'cyprus','czechia','estonia','finland','france','germany','israel','italy','lithuania',
'moldova','norway','poland','portugal','serbia','slovenia','spain','sweden','switzerland',
'ukraine','united-kingdom']

dataArr = {country:[] for country in qualCountryList}
pdJuryData = pd.read_csv('juryRank.csv', index_col = 0).astype(pd.Int64Dtype())
for row in pdJuryData.itertuples(name='Country'):
	#get Country name
	qualCountry = getattr(row, 'Index')
	for country in qualCountryList:
		#for some reason pandas dataframe refuses to get our poor child united kingdom
		#so we need to do some extra adjustments to make it work properly
		#countryStr is what we use to find where to put our row data into dataArr
		#country is the actual dataframe column name
		countryStr = country
		if country == 'united-kingdom':
			country = '_37'
			countryStr = 'united-kingdom'
		#put the value from that country's jury into array
		dataArr[countryStr].append(getattr(row, country))
print(dataArr)
#access array from dataArr['country']
binEdge = [1,6,11,16,21,26]
#fix later
for country in qualCountryList:
	sortRank = dataArr[country].sort()
	print(sortRank)