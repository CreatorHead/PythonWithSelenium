from selenium import webdriver

driver = webdriver.Chrome('C:/Users/user/Documents/dir/chromedriver.exe') #Path to the WebDriver exe file
driver.get('https://www.google.com') #open the browser and make a request to google.com
driver.maximize_window()
searchBar = driver.find_element_by_name("q"); #finds and html element by name 'q' which is the search bar
searchBar.send_keys("hello world") #pass 'hello world' inside the search bar
searchBar.submit() #submit the data to search in google or it's like clicking on the search button
driver.implicitly_wait(10000)  #Waits for 10 seconds
driver.close() #close the browser


