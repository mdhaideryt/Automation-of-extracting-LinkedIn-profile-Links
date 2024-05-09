# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import random
#
# # Update the search query
# search_query = input("Input search query: ")
#
# # Create a Chrome WebDriver instance
# driver = webdriver.Chrome()
#
# file = open('config.txt')
# lines = file.readlines()
# li_at = lines[0]
#
# # Add LinkedIn cookies
# cookies = {
#     'name': 'li_at',
#     'value': li_at,
#     'domain': '.linkedin.com',
# }
#
# # Open LinkedIn and set cookies
# driver.get("https://www.linkedin.com")
# driver.maximize_window()
# driver.add_cookie(cookies)
#
# def scroll_to_end(driver):
#     # Scroll down to the bottom of the page to load more results
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(random.uniform(2, 7))
#
# # Define the LinkedIn search URL
# search_url = f"https://www.linkedin.com/search/results/people/?keywords={search_query}"
#
# # Visit the search results page
# driver.get(search_url)
# time.sleep(random.uniform(2, 7))
#
# # Initialize variables
# profile_links = set()
# page_count = 0
#
# # Define the maximum number of pages to scrape
# max_page = 5  # Increase the number of pages to scrape
#
# while page_count < max_page:
#     scroll_to_end(driver)
#
#     # Get the page source
#     page_source = driver.page_source
#
#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(page_source, "html.parser")
#
#     # Find profile links and add them to the set
#     spans = soup.findAll('span', class_='entity-result__title-text')
#     for span in spans:
#         a_tag = span.find('a')  # Find the 'a' tag within the 'span'
#         if a_tag:
#             link = a_tag.get('href')  # Get the 'href' attribute (link)
#             profile_links.add(link)
#
#     # Check if there is a "Next" button, if not, exit
#     from selenium.webdriver.common.by import By
#
#     next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
#
#     if next_button.get_attribute("disabled") == "true":
#         break
#
#     # Click the "Next" button to load the next page of results
#     next_button.click()
#     time.sleep(random.uniform(2, 7))  # Wait for the next page to load
#     page_count += 1
#
# # Close the browser
# driver.quit()
#
# # Print and save the collected profile links
# print(f"Total number of LinkedIn profile links collected: {len(profile_links)}")
#
# import datetime
# current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# # Save the links to a text file
# with open(f'linkedin-profile-links-{search_query}_{current_time}.txt', 'w') as file:
#     for link in profile_links:
#         file.write(link + '\n')



search=input("Enter search query: ")
from selenium import webdriver
driver=webdriver.Chrome()
with open("config.txt") as f:
    li_at=f.readlines()[0]
cookies={'name':'li_at','value':li_at,'domain':'linkedin.com'}
driver.get("https://www.linkedin.com")
driver.add_cookie(cookies)
driver.maximize_window()
from bs4 import BeautifulSoup
import random
search_url=f"https://www.linkedin.com/search/results/people/?keywords={search}"
driver.get(search_url)
page=0
linkss=set()
max_page=5
while page<=max_page:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    import time
    time.sleep(random.uniform(4.2 ,7.3))
    links=BeautifulSoup(driver.page_source,'html.parser').findAll('span',class_='entity-result__title-text')
    for i in links:
        linkss.add(i.find('a').get('href'))
    from selenium.webdriver.common.by import By
    next_button=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Next"]')
    if next_button.get_attribute("disabled")==True:
        break
    next_button.click()
    time.sleep(random.uniform(3.1,5.7))
    page+=1
driver.close()
import datetime
with open(f"linkedin_profile_links_{search}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt",'w') as file:
    for i in linkss:
        file.write(i+"\n")


from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.linkedin.com')
driver.maximize_window()
with open ('config.txt') as f:
    li_at=f.readlines()[0]
cookies={'name':'li_at','value':li_at,'domain':'www.linkedin.com'}
driver.get_cookie(cookies)
inp=input('enter your query: ')
driver.get(f'https://www.linkedin.com/search/results/people/?keywords{inp}')
number=0
max=5
linkss=set()
while number<max:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    import time, random
    time.sleep(random.uniform(2.2,5.2))
    from bs4 import BeautifulSoup
    links=BeautifulSoup(driver.page_source,'html.parser').findAll('span', class_='entity-result__title-text')
    for i in links:
        linkss.add(i.find('a').get('href'))
    from selenium.webdriver.common.by import By
    next=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Next"]')
    if next.get_attribute('disabled')==True:
        break
    next.click()
    time.sleep(random.uniform(3.1,5.7))
driver.close()
import datetime
with open(f'linkedin_links_{inp}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt') as file:
    for i in linkss:
        file.write(i+"\n")


