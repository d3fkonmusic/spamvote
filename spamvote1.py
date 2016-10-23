from selenium import webdriver
import time
import sys


#driver.get("http://www.timesfreshface.com/finalists/10185")
#element = driver.find_element_by_name("Vote for me")
element = "//*[@id='467']"

def spam():
	driver.find_element_by_xpath(element).click()
	return()

def refresh():
	time.sleep(1)
	driver.refresh()
	spam()
	return()

filename = (raw_input("Enter a file name to output the number of votes cast: "))
filez = open(filename,'w')
driver=webdriver.Chrome()
driver.get("http://www.timesfreshface.com/finalists/10185")
                
for i in range(0,10000):
	print(i,)
	filez.write(str(i))
	refresh()
	
filez.close()
