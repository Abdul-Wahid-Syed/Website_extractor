from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='"C:/ChromeDriver/chromedriver-win64/chromedriver.exe"')
# Set up the Chrome driver and navigate to a web page
chrome_driver_path = service # Make sure to use forward slashes or double backslashes
chrome_options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
chrome.get('https://www.startupindia.gov.in/content/sih/en/search.html?states=5f48ce592a9bb065cdf9fb3c&stages=scaling&roles=Startup&page=1')

# Your scraping code using Selenium here
# For example, find elements by their CSS selectors
elements = chrome.find_elements(By.CSS_SELECTOR, '.category-card.search-card.new-eco-card a')
for element in elements:
    href = element.get_attribute('href')
    print(f'Found href: {href}')

# Close the browser when you're done
chrome.quit()
