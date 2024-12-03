from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.select import Select
from time import sleep
from tqdm import tqdm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import openpyxl

dealer_data = {
    "Category Type": [],
    "Name": [],
    "Dealer Name": [],
    "Address": [],
    "Contact": [],
    "Phone": [],
    "Email": [],
    "Website": []
}

ua = UserAgent()
user_agent = ua.random
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")  # Tarayıcı penceresini manuel olarak ayarla
options.add_argument("--disable-gpu")  # GPU kaynaklı sorunları önlemek için (genellikle Windows'ta kullanılır)
options.add_argument("--disable-dev-shm-usage")  # Paylaşılan bellek kullanımını devre dışı bırakır

options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(options=options)
driver.get("https://www.milnor.com/dealers/#searchByLocation")
sleep(5)
category_buttons = driver.find_elements(By.CSS_SELECTOR, "ul.list-unstyled li label")

for i in range(len(category_buttons)):
    category_buttons = driver.find_elements(By.CSS_SELECTOR, "ul.list-unstyled li label")
    category = category_buttons[i]
    if not category.is_selected() :
        category.click()
        sleep(2)
    category_text = category.text
    country_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "countryIDSelect")))
    select_1 = Select(country_button)
    select_1.select_by_visible_text("United States Of America")

    state_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "stateIDSelect")))
    state_list = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select#stateIDSelect option")))
    state_list = [state.text for state in state_list][2:]
    for state in tqdm(state_list, desc="State is scrapping...", total=len(state_list), ncols=100, colour="blue"):
        try:
            # State seçim işlemi
            state_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "stateIDSelect")))
            select_2 = Select(state_button)
            select_2.select_by_visible_text(state)
            sleep(2)
            
            # County kontrol ve liste alma
            counties = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "select#countyIDSelect option")))
            county_list = [county.text for county in counties][2:]
    
            for county_name in tqdm(county_list, desc="State is scrapping...", total=len(county_list), ncols=100, colour="green"):
                try:
                    county_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "countyIDSelect")))
                    select_3 = Select(county_element)
                    select_3.select_by_visible_text(county_name)
                    sleep(1)
                    
                    # Dealer kontrolü
                    dealers = WebDriverWait(driver, 2.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.dealerResult")))
                    for dealer in dealers:
                        try:
                            name = dealer.find_element(By.CSS_SELECTOR, "div.dealerCompanyName h4").text
                        except:
                            name = "Empty"
                        
                        try:
                            dealer_name = dealer.find_element(By.CSS_SELECTOR, "div.dealerName h4").text
                        except:
                            dealer_name = "Empty"
                        
                        try:
                            address_text = dealer.find_element(By.CSS_SELECTOR, "div.dealerAddress").text
                            address = address_text.replace("\n", ", ")
                        except:
                            address = "Empty"
                        
                        try:
                            contact_text = dealer.find_element(By.CSS_SELECTOR, "div.dealerContact").text
                            contact = contact_text.split(":")[1].strip() if ":" in contact_text else "Empty"
                        except:
                            contact = "Empty"
                        
                        try:
                            phone_numbers = [phone.text for phone in dealer.find_elements(By.CSS_SELECTOR, "div.dealerPhone1 a")]
                            phone = ", ".join(phone_numbers) if phone_numbers else "Empty"
                        except:
                            phone = "Empty"
                        
                        try:
                            email_numbers = [email.text for email in dealer.find_elements(By.CSS_SELECTOR, "div.contactEmail1 a")]
                            email = ", ".join(email_numbers) if email_numbers else "Empty"
                        except:
                            email = "Empty"
                        
                        try:
                            website = dealer.find_element(By.CSS_SELECTOR, "div.contactURL a").text
                        except:
                            website = "Empty"

                        dealer_data["Category Type"].append(category_text)
                        dealer_data["Name"].append(name)
                        dealer_data["Dealer Name"].append(dealer_name)
                        dealer_data["Address"].append(address)
                        dealer_data["Contact"].append(contact)
                        dealer_data["Phone"].append(phone)
                        dealer_data["Email"].append(email)
                        dealer_data["Website"].append(website)

                except TimeoutException:
                    print(f"Dealer is not found for county: {county_name}")
                except Exception as e:
                    print(f"Unexpected error for county: {county_name} - {e}")
        except TimeoutException:
            print(f"County is not found for state: {state}")
            try:
                # Eğer county bulunamıyorsa, state'te genel dealer arama
                dealers = WebDriverWait(driver, 2.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.dealerResult")))
                for dealer in dealers:
                    try:
                        name = dealer.find_element(By.CSS_SELECTOR, "div.dealerCompanyName h4").text
                    except:
                        name = "Empty"
                    
                    try:
                        dealer_name = dealer.find_element(By.CSS_SELECTOR, "div.dealerName h4").text
                    except:
                        dealer_name = "Empty"
                    
                    try:
                        address_text = dealer.find_element(By.CSS_SELECTOR, "div.dealerAddress").text
                        address = address_text.replace("\n", ", ")
                    except:
                        address = "Empty"
                    
                    try:
                        contact_text = dealer.find_element(By.CSS_SELECTOR, "div.dealerContact").text
                        contact = contact_text.split(":")[1].strip() if ":" in contact_text else "Empty"
                    except:
                        contact = "Empty"
                    
                    try:
                        phone_numbers = [phone.text for phone in dealer.find_elements(By.CSS_SELECTOR, "div.dealerPhone1 a")]
                        phone = ", ".join(phone_numbers) if phone_numbers else "Empty"
                    except:
                        phone = "Empty"
                    
                    try:
                        email_numbers = [email.text for email in dealer.find_elements(By.CSS_SELECTOR, "div.contactEmail1 a")]
                        email = ", ".join(email_numbers) if email_numbers else "Empty"
                    except:
                        email = "Empty"
                    
                    try:
                        website = dealer.find_element(By.CSS_SELECTOR, "div.contactURL a").text
                    except:
                        website = "Empty"

                    dealer_data["Category Type"].append(category_text)
                    dealer_data["Name"].append(name)
                    dealer_data["Dealer Name"].append(dealer_name)
                    dealer_data["Address"].append(address)
                    dealer_data["Contact"].append(contact)
                    dealer_data["Phone"].append(phone)
                    dealer_data["Email"].append(email)
                    dealer_data["Website"].append(website)
                    
            except TimeoutException:
                print(f"Dealer is not found for state: {state}")
            except Exception as e:
                print(f"Unexpected error for state: {state} - {e}")
        except Exception as e:
            print(f"Unexpected error for state: {state} - {e}")


unique_data = list({(category_type,name,dealer_name,address,contact,phone,email,website) for category_type,name,dealer_name,address,contact,phone,email,website in zip(
    dealer_data["Category Type"],
    dealer_data["Name"],
    dealer_data["Dealer Name"],
    dealer_data["Address"],
    dealer_data["Contact"],
    dealer_data["Phone"],
    dealer_data["Email"],
    dealer_data["Website"]
)})

clean_data = {
    "category_type" : [item[0] for item in unique_data],
    "name" : [item[1] for item in unique_data],
    "dealer name" : [item[2] for item in unique_data],
    "address" : [item[3] for item in unique_data],
    "contact" : [item[4] for item in unique_data],
    "phone" : [item[5] for item in unique_data],
    "email" : [item[6] for item in unique_data],
    "website" : [item[7] for item in unique_data],
}

df = pd.DataFrame(clean_data)
ydf = df.sort_values(["category_type"])
ydf.to_excel("distributors_2.xlsx", index=False)
df.to_csv("distributors_2csv.csv", index=False)