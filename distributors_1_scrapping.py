from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.select import Select
from time import sleep
from tqdm import tqdm
import pandas as pd
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dict = {
    "name" : [],
    "address" : [],
    "toll free" : [],
    "local phone" : [],
    "email" : [],
    "website" : []
}

ua = UserAgent()
user_agent = ua.random
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(options=options)
driver.get("https://dexter.com/distributor-locator/")
sleep(5)
state_tag = driver.find_element(By.ID, "state")
option_tags = state_tag.find_elements(By.CSS_SELECTOR, "optgroup[label='State'] option")
option_list = [tag.text for tag in option_tags]
select_1 = Select(state_tag)
sleep(1)
for option in tqdm(option_list, desc= "State is scrapping...", ncols = 100, total = len(option_list), colour='blue'):
    select_1.select_by_visible_text(option)
    sleep(1)
    county_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "county")))
    county_tag = county_.find_elements(By.CSS_SELECTOR, "option")
    county_list = [county.text for county in county_tag]
    sleep(1)
    select_2 = Select(county_)
    for county in tqdm(county_list, desc= "County is scrapping...", ncols =100, total =len(county_list), colour='green', leave=False):
        select_2.select_by_visible_text(county)
        sleep(1)
        li_list = []
        sleep(1.5)
        if driver.find_elements(By.CSS_SELECTOR, "div.locator-results ul.locator-list div.rl-content ul.locator-address"):
            li_list = driver.find_elements(By.CSS_SELECTOR, "div.locator-results ul.locator-list div.rl-content")
            if len(li_list) >= 1:
                for li in li_list:
                    try:
                        name = li.find_element(By.CSS_SELECTOR, "h3").text
                    except:
                        name = "Empty"
                    dict["name"].append(name)

                    li_text = li.find_element(By.CSS_SELECTOR, "ul").text
                    li_text = li_text.split("\n")
                    address = " - ".join(li_text[:3])
                    dict["address"].append(address)
                
                    li_text = li_text[3:]
                    toll_free = "Empty"
                    local_phone = "Empty"
                    email = "Empty"
                    website = "Empty"
            
                    for item in li_text:
                        if "Toll Free" in item:
                            toll_free = item.split(":")[1].strip()
                        elif "Local Phone" in item:
                            local_phone = item.split(":")[1].strip()
                        elif "@" in item:
                            email = item
                        elif "http" in item:
                            website = item
                    dict["toll free"].append(toll_free)
                    dict["local phone"].append(local_phone)
                    dict["email"].append(email)
                    dict["website"].append(website)

unique_data = list({(name,address,tollfree,localphone,email,website) for name,address,tollfree,localphone,email,website in zip(
    dict["name"],
    dict["address"],
    dict["toll free"],
    dict["local phone"],
    dict["email"],
    dict["website"]
)})
cleaned_date = {
    "name" : [item[0] for item in unique_data],
    "address" : [item[1] for item in unique_data],
    "toll free" : [item[2] for item in unique_data],
    "local phone" : [item[3] for item in unique_data],
    "email" : [item[4] for item in unique_data],
    "website" : [item[5] for item in unique_data],
}

df = pd.DataFrame(cleaned_date)
df.to_excel("distributors_1.xlsx", index=False)
df.to_csv("distributors_1csv.csv", index=False)
