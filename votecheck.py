from selenium import webdriver
import time
import sys

element1 = "//*[@id='515']" #client
element = "//*[@id='467']"  #client

def refresh(sleeptime):
    time.sleep(sleeptime)
#    driver1.refresh()
    driver2.refresh()
    return()

#def spam():
#    driver1.find_element_by_xpath(element).click()
#    return()

def checkCompete():
    checkvotes = driver2.find_element_by_xpath(element1)
    element_attribute_value = checkvotes.get_attribute('value')
    value = (format(element_attribute_value))
    return value

def checkClient():
    checkvotes = driver2.find_element_by_xpath(element)
    element_attribute_value = checkvotes.get_attribute('value')
    value = (format(element_attribute_value))
    return value

sleeptime = int(input("Enter the refresh time in seconds (sec): "))

#driver1=webdriver.Chrome()
driver2=webdriver.Chrome()

#driver1.get("http://www.timesfreshface.com/finalists/10185")
driver2.get("http://www.timesfreshface.com/bangalore")

for i in range(0,10000):
    print(" Chummi = ",checkClient()," Contestant = ",checkCompete())
#    spam()
    refresh(sleeptime)
