from selenium import webdriver
import time
import sys

id1 = "//*[@id='467']"  #client
id2 = "//*[@id='515']" #contestant

def refresh(sleeptime):
    time.sleep(sleeptime)
#    driver1.refresh()
    driver2.refresh()
    return()

#def spam():
#    driver1.find_element_by_xpath(element).click()
#    return()

def checkVotes(idx):
    checkvotes = driver2.find_element_by_xpath(idx)
    element_attribute_value = checkvotes.get_attribute('value')
    value = (format(element_attribute_value))
    return value

sleeptime = int(input("Enter the refresh time in seconds (sec): "))

#driver1=webdriver.Chrome()
driver2=webdriver.Chrome()

#driver1.get("http://www.timesfreshface.com/finalists/10185")
driver2.get("http://www.timesfreshface.com/bangalore")

for i in range(0,10000):
    print(" Client = ",checkVotes(id1)," Contestant = ",checkVotes(id2))
#    spam()
    refresh(sleeptime)
