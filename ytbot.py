from selenium import webdriver
from time import sleep

driver1= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")#In executable path give the path of chromedriver that you have downloaded. In my case it is in downloads.
driver2= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")
driver3= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")

driver1.get("https://youtu.be/OU69JaZ1FQo")#provide the link
driver2.get("https://youtu.be/OU69JaZ1FQo")
driver3.get("https://youtu.be/OU69JaZ1FQo")
#i have used driver 1,2,3  so it will open 3 tabs 
#if you want to add more tabs you can also do it 

while True:
    sleep(18)#sleep 18 meanes after 18 seconds page will refresh
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    
    #To execute - Simple run this code
    #Happy coding - Siddharth
