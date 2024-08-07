from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_wp_res = response.text

soup = BeautifulSoup(zillow_wp_res, "html.parser")

# Find Links
links = []
link_list = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

for x in range(0, len(links)):
    if "zillow" in links[x]:
        link_list.append(links[x])

link_list = list(set(link_list[1:]))

# Find Prices
prices = []
prices_list = []
for price in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine"):
    prices.append(price.text)

for x in range(0, len(prices)):
    if "+/mo" in prices[x]:
        prices[x] = prices[x].strip("+/mo")
    if "/mo" in prices[x]:
        prices[x] = prices[x].strip("/mo")
    if "+ 1 bd" in prices[x]:
        prices[x] = prices[x].strip("+ 1 bd")
    if "+ 1bd" in prices[x]:
        prices[x].replace("+ 1bd", "")

    prices_list.append(prices[x])

# Find addresses
addresses = []
addresses_list = []

for add in soup.findAll(name="img", class_="Image-c11n-8-84-listing"):
    addresses.append(add.get("alt"))

for x in range(0, len(addresses)):
    if "|" in addresses[x]:
        addresses[x] = addresses[x].replace("|", " ")
    if "  " in addresses[x]:
        addresses[x] = addresses[x].replace("  ", "")

    addresses_list.append(addresses[x])

# end of bs4 operation


# start selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

for i in range(0, len(addresses)):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScZQevn8rVRt1CPGrsFEfJUYOpEkjst-k5orqCoVIkNM-E21w/viewform?vc=0&c=0&w=1&flr=0&usp=mail_form_link")
    time.sleep(3)

    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.click()
    address_input.send_keys(addresses_list[i])
    time.sleep(1)

    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(prices_list[i])
    time.sleep(1)

    link_input = driver.find_element(By.XPATH,
                                     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(link_list[i])
    time.sleep(1)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    time.sleep(3)

    driver.close()
