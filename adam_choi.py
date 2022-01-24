from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '<path to chromedriver>'
driver = webdriver.Chrome(path)
driver.get(website)

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Italy')

time.sleep(1)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

time.sleep(1)

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home_team.append(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

driver.quit()

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('scores_data.csv', index=False)
print(df)
