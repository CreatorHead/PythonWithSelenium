from selenium import webdriver

driver = webdriver.Chrome('C:/Users/user/Documents/dir/chromedriver.exe')  # Path to the WebDriver exe file
driver.get('https://www.google.com')  # open the browser and make a request to google.com
driver.maximize_window()
searchBar = driver.find_element_by_name("q");  # finds and html element by name 'q' which is the search bar
searchBar.send_keys("hello world")  # pass 'hello world' inside the search bar
searchBar.submit()  # submit the data to search in google or it's like clicking on the search button
driver.implicitly_wait(10000)  # Waits for 10 seconds
driver.close()  # close the browser

first_name = driver.find_element_by_id("firstname")
last_name = driver.find_element_by_id("lastname")
email_address = driver.find_element_by_id("email")
news_letter_subscription = driver.find_element_by_id('news_letter')
password = driver.find_element_by_id('password')
submit_button = driver.find_element_by_id('submit')
confirm_password = driver.find_element_by_id('confirm_password')

# check new user is registered
if driver.find_element_by_css_selector("p.hello > strong").text() == "Hello, Test User1!":
    print('Login Successful')
else:
    print('Login Failed')

if driver.find_element_by_link_text("Log Out").is_displayed():
    print("Logout button is Displayed")
else:
    print("Logout button is not displaying")
