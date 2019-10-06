from selenium import webdriver

driver = webdriver.Chrome('C:/Users/user/Documents/dir/chromedriver.exe') #Path to the WebDriver exe file
driver.get('https://www.google.com') #open the browser and make a request to google.com
driver.maximize_window()
driver.implicitly_wait(10000)  #Waits for 10 seconds
driver.close() #close the browser



