from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
import usaddress
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



def perform_scraping_san_mateo(address_string, browser, headless, chrome_path, firefox_path):
    # Create a new instance of the Chrome driver
    # options["executable_path"] = "/Users/apoorv/Hausable/selenium_scraping/chromedriver"
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options = Options()
    # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    # For Scraping in local
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/chromedriver")
    # browser = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe"))

    # go to the google home page


    #For scraping in Firefox
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/geckodriver", firefox_options=options)

    if browser == "firefox":
        options = Options()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path = firefox_path, firefox_options=options)
    elif browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        capabilities = {
          'browserName': 'chrome',
          'chromeOptions':  {
            'useAutomationExtension': False,
            'forceDevToolsScreenshot': True,
            'args': ['--start-maximized', '--disable-infobars']
          }
        }    
        if headless:
            chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = chrome_path)



    driver.get("http://maps.smcgov.org/GE_4_4_0_Html5Viewer_2_5_0_public/?viewer=raster")

    
    





    try:
        WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH,"//button[@title='Search parcels by address']")))

        WebDriverWait(driver, 100).until( EC.invisibility_of_element_located((By.CLASS_NAME,"splash-overlay")))
        address_button = driver.find_element_by_xpath("//button[@title='Search parcels by address']//p")
        WebDriverWait(driver, 100).until( EC.invisibility_of_element_located((By.CLASS_NAME,"splash-overlay")))
        address_button.click()

        


        WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH,"//div[@class='form-control']//div[@class='autocomplete-input']//input")))

        address_bar = driver.find_element_by_xpath("//div[@class='form-control']//div[@class='autocomplete-input']//input")
        address_bar.click()
        address_bar.send_keys(address_string)

        # driver.execute_script("document.evaluate(\"//div[@class='form-control']//div[@class='autocomplete-input']//input\" ,document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value = '527 miller ave, south san francisco';") 


        
        # WebDriverWait(driver, 100).until( EC.invisibility_of_element_located((By.CLASS_NAME,"loader bound-visible")))


        # wait = ui.WebDriverWait(driver,10)
        

        submit_button = driver.find_element_by_xpath("//div[@class='form-btns']//button[contains(text(), 'Search')]")
        submit_button.click()

        # driver.execute_script("document.evaluate(\"//div[@class='form-btns']//button[contains(text(), 'Search')]\" ,document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")

        # WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.CLASS_NAME,"loading-container bound-invisible")))
        WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH,"//span[@class='list-menu-details']//button")))

        # WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.CLASS_NAME,"list-menu-name bound-visible")))

        result = driver.find_element_by_xpath("//span[@class='list-menu-details']//button")
        print(result.text)

        map_link = driver.find_element_by_xpath("//span[@class='list-menu-details']//span//div//a[@download='']")
        print(map_link.text)
        a = map_link.get_attribute("href")

        all_data = {}
        all_data["map_link"] = a

        print(all_data)

        return all_data


    except Exception as e:
        print(e)
        all_data = {}
        all_data["apn"] = "Something Went wrong"

        print(all_data)
        return "OK"



    finally:
        pass
        # driver.quit()



# print(perform_scraping_san_mateo('527 miller ave, south san francisco'))


