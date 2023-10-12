# from selenium1 import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

# url = "https://www.naver.com"
# driver.get(url)
# time.sleep(5)


from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)

a = driver.find_element_by_css_selector()
print(a)