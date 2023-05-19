from selenium import webdriver
import pandas as pd

driver = webdriver.Firefox()
#eventually make a whole ass loop where the ending is the country name appended to the url
driver.get('https://eurovision.tv/event/liverpool-2023/grand-final/results/albania')
#absolute XPATH because I have no idea how to do relative yet
table = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/main/section/div/div[2]/div/div/div[2]/div/div/div[2]/div/table')
#find first(?) instance of rank, which would be jury vote rank
print(table.find_element(By.CLASS_NAME, 'Rank'))
driver.quit()
