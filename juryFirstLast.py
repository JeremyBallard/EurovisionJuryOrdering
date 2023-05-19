from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
#every country that votes
fullCountryList = ['albania', 'armenia', 'australia', 'austria', 'azerbaijan', 'belgium', 
'croatia', 'cyprus', 'czechia', 'denmark', 'estonia', 'finland', 'france', 'georgia', 
'germany', 'greece', 'iceland', 'ireland', 'israel', 'italy', 'latvia', 'lithuania',
'malta', 'moldova', 'netherlands', 'norway', 'poland', 'portugal', 'romania',
'san-marino', 'serbia', 'slovenia', 'spain', 'sweden', 'switzerland', 'ukraine',
'united-kingdom']
#every country that can receive jury votes
qualCountryList = ['albania', 'armenia', 'australia', 'austria', 'belgium', 'croatia',
'cyprus','czechia','estonia','finland','france','germany','israel','italy','lithuania',
'moldova','norway','poland','portugal','serbia','slovenia','spain','sweden','switzerland',
'ukraine','united-kingdom']
#generates unique dictionary with no data for each country
countryDict = {key:[] for key in qualCountryList}
driver = webdriver.Firefox()
driver.implicitly_wait(2)
#loop for each voting country's full results
#37 because range is exclusive at the end
for i in range(0,37):
	driver.get('https://eurovision.tv/event/liverpool-2023/grand-final/results/' + fullCountryList[i])
	#absolute XPATH because I have no idea how to do relative yet
	tableXPath = '/html/body/div[1]/div/div/div[3]/div/div/main/section/div/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody'
	#A country can't vote for itself, add None to space
	if fullCountryList[i] in qualCountryList:
		countryDict[fullCountryList[i]].append(None)
	#iterate through and find jury rank to each other country
	for j in range(1,26):
		countryXPath = tableXPath + '/tr[' + str(j) +']/td[1]'
		juryXPath = tableXPath + '/tr[' + str(j) +']/td[8]'
		#EBU likes formal spelling but breaks key matching
		country = driver.find_element(By.XPATH, countryXPath).text.lower()
		#necessary to match up keys properly
		country = country.replace(" ", "-")
		juryRank = driver.find_element(By.XPATH, juryXPath).text
		#https://www.guru99.com/python-dictionary-append.html
		#takes name of country, uses it as a key for the correct dictionary
		#then adds respective country's jury rank
		countryDict[country].append(juryRank)
	time.sleep(.5)
pdFullCountryData = pd.DataFrame.from_dict(countryDict, orient='index', 
						columns=fullCountryList)
print(pdFullCountryData)


driver.close()
driver.quit()
