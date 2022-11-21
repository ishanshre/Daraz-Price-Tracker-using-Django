#from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
options.headless = True
options.add_argument("--window-size=1366,768")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
def get_detail(url):
    driver.get(url)
    title = driver.find_element(by=By.XPATH, value='//*[@id="module_product_title_1"]/div/div/span')
    current_price = driver.find_element(by=By.XPATH, value='//*[@id="module_product_price_1"]/div/div/span')
    original_price = driver.find_element(by=By.XPATH, value='//*[@id="module_product_price_1"]/div/div/div/span[1]')
    seller = driver.find_element(by=By.XPATH, value='//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a')

    product = {
        'title':title.text,
        'current_price':float(current_price.get_attribute('innerHTML')[4:].replace(',','')),
        'original_price':float(original_price.get_attribute('innerHTML')[4:].replace(',','')),
        'seller':seller.text
    }
    return product



# def getDetail(url):
#     s = HTMLSession()
#     r = s.get(url)
#     r.html.render(sleep=1)
    
#     product = {
#         'title' : r.html.xpath('//*[@id="module_product_title_1"]/div/div/span', first=True).text,
#         'current_price': float(r.html.xpath('//*[@id="module_product_price_1"]/div/div/span', first=True).text[4:].replace(',','')),
#         'original_price': float(r.html.xpath('//*[@id="module_product_price_1"]/div/div/div/span[1]', first=True).text[4:].replace(',','')),
#         "seller":r.html.xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a[1]', first=True).text,
#     }
#     return product
