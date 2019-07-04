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




def perform_scraping_sfo(address_string, browser, headless, chrome_path, firefox_path):
    # Create a new instance of the Chrome driver
    # options["executable_path"] = "/Users/apoorv/Hausable/selenium_scraping/chromedriver"

    # capabilities = {
    #   'browserName': 'chrome',
    #   'chromeOptions':  {
    #     'useAutomationExtension': False,
    #     'forceDevToolsScreenshot': True,
    #     'args': ['--start-maximized', '--disable-infobars']
    #   }
    # }    


    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # #### chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--proxy-server='direct://'")
    # chrome_options.add_argument("--proxy-bypass-list=*")


    # # For Scraping in local
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/chromedriver")


    # #For scraping in Firefox
    # # options = Options()
    # # options.add_argument("--headless")
    # # driver = webdriver.Firefox(executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/geckodriver", firefox_options=options)

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



    driver.get("https://sfplanninggis.org/pim/")

    
    


    # try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    # pass

    # title = driver.find_element_by_class_name("panel-title")
    # print(title)
    WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID,"addressInput")))

    address_bar = driver.find_element_by_id("addressInput")
    address_bar.click()
    address_bar.send_keys(address_string)

    address_bar.click()
    address_bar.send_keys(Keys.RETURN)

    # search_button = driver.find_element_by_id("Search-icon")
    # search_button.click()
    # driver.execute_script("arguments[0].click();", search_button)
    # webdriver.ActionChains(driver).move_to_element(search_button).click(search_button).perform()
    # driver.execute_script("throttleSubmit(document.getElementById('addressInput').value)")
 
    WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID,"AssessorBlockMap")))


    WebDriverWait(driver, 10).until( EC.text_to_be_present_in_element((By.ID,"AssessorBlockMap"), "Assessor's Block Map"))
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "AssessorBlockMap")))

    map_link = driver.find_element_by_id("AssessorBlockMap")
    print(map_link.text)
    print(map_link.get_attribute("href"))

    all_data = {}
    all_data["map_link"] = map_link.get_attribute("href")

    return all_data

      	


    # except Exception as e:
    #     print(e)
    #     all_data = {}
    #     all_data["apn"] = "Something Went wrong"
    #     return all_data

    # finally:
    #     pass
    #     # driver.quit()



# print(perform_scraping_sfo('1557 fulton st'))


