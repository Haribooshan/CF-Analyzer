from CF_API import getInfoFromAPI

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

username = "haribooshan2003"
base_url = "https://codeforces.com"

os.environ["PATH"] += r"C:\Users\harib\Documents\CODING\Web Dev\FreeCodeCamp\Selenium\Selenium_Drivers\chrome-headless-shell-win64"

# Initializing WebDriver with headless option for faster execution
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

# driver.implicitly_wait(5)

driver.get(f"{base_url}/contests/with/{username}")

# time.sleep(5)


# TableElement = driver.find_element(By.CLASS_NAME,"user-contests-table")
TableElement = driver.find_element(By.CSS_SELECTOR,'table.user-contests-table')
Cards = TableElement.find_elements(By.TAG_NAME,'tr')

ContestTable = []

for i in range(1,len(Cards)):
    ContestTable.append(Cards[i].find_elements(By.TAG_NAME,'td')) # Retrieves all td children.

d = dict()

# For debugging purposes use 'outerHTML' attribute.
# The .text attribute is really cool.
# XPath is very cool, try to use that.

ContestsDict = dict()

for contest in ContestTable :
    
    Number = int(contest[0].get_attribute("innerHTML").strip())
    Id = contest[1].find_element(By.TAG_NAME,'*').get_attribute('href').split('/')[-1].strip()
    
    Date = contest[2].find_element(By.TAG_NAME,'a').text.split(' ')[0].strip()
    Rank = contest[3].text
    
    StandingsLink = contest[3].find_element(By.TAG_NAME,'a').get_attribute('href')
    # StandingsLink = contest[3].find_element(By.TAG_NAME,'a')

    ProblemsSolved = contest[4].text

    ContestsDict[Number] = { 'Id' : Id ,'Date' : Date , 'Rank' : Rank , 'StandingsLink' : StandingsLink ,
                            'ProblemsSolved' : ProblemsSolved }

# Printing the results until now.
# for key,val in ContestsDict.items() :
    # print(key,val)

# Works, but seems to be quite slow.

# print(ContestsDict[3]['ProblemsSolved'])

# driver.quit()

# for ContestNumber in ContestsDict :
#     link = ContestsDict[ContestNumber]['StandingsLink']
#     driver.get(link)
#     driver.back()

# This takes very long, like 2mins, how to speed it up ?. Any Alternative ?.


for key,val in ContestsDict.items() :
    print(val['Id'])



