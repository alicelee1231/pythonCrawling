# from selenium import webdriver
# import time

# #step1. 사용자에게 검색 관련 정보들을 입력받기
# print("="*100)
# print("Those data was from NAVER")
# print("="*100)

# date_text = int(input('please enter the date which one you want to search'))
# print('\n')

# chrome_path = "Users/isaemmi/Desktop/pythonCra/chromedriver.exe"
# driver = webdriver.Chrome(chrome_path)

# url = "https://finance.naver.com/news/"
# driver.get(url)
# time.sleep(2)

# driver.maximize_window()
# time.sleep(2)

# element=driver.find_element_by_id("media_end_head_info_datestamp_time _ARTICLE_DATE_TIME")
# driver.find_element_by_id("media_end_head_info_datestamp_time _ARTICLE_DATE_TIME").click()
# element.send_keys(date_text+"\n")

from selenium import webdriver
import time

# Step 1: Collect user input for the date
print("=" * 100)
print("This data is from NAVER")
print("=" * 100)

date_text = input('Please enter the date (yyyy-mm-dd) you want to search: ')
print('\n')

# Step 2: Set up the web driver
driver = webdriver.Chrome()

url = "https://finance.naver.com/news/"
driver.get(url)
time.sleep(2)

# Step 3: Locate and interact with the search input field
search_input = driver.find_element_by_name("search")
search_input.send_keys(date_text)
search_input.submit()

# Wait for the results to load (you can increase the time if needed)
time.sleep(5)

# Now, you can scrape the news articles based on the search results.
# You should write code to extract the desired information from the search results page.
# This might involve finding and clicking on news articles or extracting their titles and links.
# Please note that web scraping may have legal and ethical considerations, so make sure you have the right to access and use this data.
