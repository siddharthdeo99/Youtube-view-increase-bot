from selenium import webdriver
from time import sleep

driver1= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")
driver2= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")
driver3= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")

driver1.get("https://youtu.be/OU69JaZ1FQo")
driver2.get("https://youtu.be/OU69JaZ1FQo")
driver3.get("https://youtu.be/OU69JaZ1FQo")

while True:
    sleep(18)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()