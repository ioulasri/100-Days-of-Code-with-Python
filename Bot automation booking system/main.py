from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome("/Users/imadoulasri/Documents/chromedriver", options=chrome_options)

driver.get("https://demo.anhtester.com/input-form-demo.html")

driver.maximize_window()

