import pandas as pd

#import csv table into dataframe
#index_col = 0 to remove extra index column, easier for using country ID directly
#https://stackoverflow.com/questions/12960574/pandas-read-csv-index-col-none-not-working-with-delimiters-at-the-end-of-each-li
#https://stackoverflow.com/questions/21287624/convert-pandas-column-containing-nans-to-dtype-int
juryFullRank = pd.read_csv('juryRank.csv', index_col = 0).astype(pd.Int64Dtype())
lastDict = {}
firstDict = {}
qualifiedList = []
#https://stackoverflow.com/questions/28218698/how-to-iterate-over-columns-of-pandas-dataframe-to-run-regression
for column in juryFullRank:
	columnDict = juryFullRank[column].to_dict()
	#https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value
	#any finds if there's a 0, which means lowest rank is 25, not 26
	if(any(x == 0 for x in list(columnDict.values()))):
		lastDict[column] = list(columnDict.keys())[list(columnDict.values()).index(25)]
		#add country as qualified for later use
		qualifiedList.append(column)
	else:
		lastDict[column] = list(columnDict.keys())[list(columnDict.values()).index(26)]
	firstDict[column] = list(columnDict.keys())[list(columnDict.values()).index(1)]
#dictionary that has country jury as key and 2 values in array, the first value being first place
#the second being last place
juryFirstLastPlaces = {country:[] for country in firstDict.keys()}
#we only count the countries that qualified
firstLastCount = {country:[0,0] for country in qualifiedList}
#merge first and last place together into this dictionary, following rules established earlier
#counting every time a country gets added into first or last column respectively
#can do this because keys are in the same order, effectively a list? But also not?
for country in firstDict.keys():
	juryFirstLastPlaces[country].append(firstDict[country])
	#firstLastCount[0] is first place
	firstLastCount[firstDict[country]][0] += 1
	juryFirstLastPlaces[country].append(lastDict[country])
	#firstLastCount[1] is last place
	firstLastCount[lastDict[country]][1] += 1
#output DataFrame and then to csv for data save
pdJuryFirstLast = pd.DataFrame.from_dict(juryFirstLastPlaces, orient='index',
						columns=['Jury First','Jury Last'])
pdJuryCount = pd.DataFrame.from_dict(firstLastCount, orient='index',
						columns=['# of First', '# of Last'])
pdJuryFirstLast.to_csv("juryFirstLast.csv")
pdJuryCount.to_csv('juryCount.csv')