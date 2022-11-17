from selenium import webdriver
#
# my_driver = webdriver.Chrome(executable_path=r'C:\Users\itamara\Downloads\chromedriver\chromedriver.exe')
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

# google = driver.get("https://www.google.com")

google = driver.get(r'C:\Users\itamara\Downloads\tip_calc\tip_calc\index.html')

# driver.find_element(By.ID, "billamt").send_keys('100')
driver.find_element(By.XPATH, '//*[@id="billamt"]').send_keys('100')
# driver.find_element(By.XPATH("//input[@id='retrieveButton-btnInnerEl']")).send_keys('10')

driver.find_element(By.XPATH, '//*[@id="serviceQual"]/option[2]').click()
driver.find_element(By.ID, "peopleamt").send_keys('5')
driver.find_element(By.ID, 'calculate').click()

tip_result = driver.find_element(By.ID, 'tip').text
assert tip_result == "6.00"
print(google)

# id="billamt"
