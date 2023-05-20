import pandas as pd

#import csv table into dataframe
#index_col = 0 to remove extra index column, easier for country ID later
#https://stackoverflow.com/questions/12960574/pandas-read-csv-index-col-none-not-working-with-delimiters-at-the-end-of-each-li
#https://stackoverflow.com/questions/21287624/convert-pandas-column-containing-nans-to-dtype-int
juryFullRank = pd.read_csv('juryRank.csv', index_col = 0).astype(pd.Int64Dtype())
lastDict = {}
firstDict = {}
#https://stackoverflow.com/questions/28218698/how-to-iterate-over-columns-of-pandas-dataframe-to-run-regression
for column in juryFullRank:
	columnDict = juryFullRank[column].to_dict()
	#https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value
	#any finds if there's a 0, which means lowest rank is 25, not 26th
	if(any(x == 0 for x in list(columnDict.values()))):
		lastDict[column] = list(columnDict.keys())[list(columnDict.values()).index(25)] + ' last'
	else:
		lastDict[column] = list(columnDict.keys())[list(columnDict.values()).index(26)] + ' last'
	firstDict[column] = list(columnDict.keys())[list(columnDict.values()).index(1)] + ' first'
#https://stackoverflow.com/questions/5946236/how-to-merge-dicts-collecting-values-from-matching-keys
#since keys are in order, and .values() outputs a list, zip lists, then take keys and match to zipped val list
keys = firstDict.keys()
vals = zip(firstDict.values(), lastDict.values())
juryFirstLastPlaces = dict(zip(keys, vals))
print(juryFirstLastPlaces)
