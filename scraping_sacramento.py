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




def perform_scraping_sacramento(address_string, browser, headless, chrome_path, firefox_path):
    # Create a new instance of the Chrome driver
    # options["executable_path"] = "/Users/apoorv/Hausable/selenium_scraping/chromedriver"
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options = Options()
    # # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    # For Scraping in local
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/chromedriver")
    # browser = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe"))

    # go to the google home page


    


    # chrome_options = webdriver.ChromeOptions()
    # # chrome_options.add_argument('--headless')
    # #### chrome_options.add_argument('--disable-gpu')
    


    # # # For Scraping in local
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/chromedriver", desired_capabilities=capabilities)



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
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = chrome_path, desired_capabilities=capabilities)

    driver.get("http://assessorparcelviewer.saccounty.net/JSViewer/assessor.html")






    try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    # pass

    # title = driver.find_element_by_class_name("panel-title")
    # print(title)
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID,"Map1_BASE_MAP_LABELS")))


        print(driver.title)


        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID,"PopupDisclaimer")))

        # driver.execute_script("document.getElementById('PopupDisclaimer').scrollTop = 100")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'ACCEPT')]")))

        accept_button = driver.find_element_by_xpath("//button[contains(text(), 'ACCEPT')]")

        accept_button.click()

        WebDriverWait(driver, 10).until( EC.invisibility_of_element_located((By.CLASS_NAME,"modal-backdrop fade")))

        address_bar = driver.find_element_by_id("omniInput")
        address_bar.send_keys(address_string)

        address_bar.click()
        address_bar.send_keys(Keys.RETURN)

        

        # search_button = driver.find_element_by_id("goOmniSearch")
        # search_button.click()



        print("*"*10)

        

        # WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.ID,"parcelimagetext")))

        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID,"ParcelAPNLabel")))

        WebDriverWait(driver, 10).until( EC.text_to_be_present_in_element((By.ID,"ParcelAPNLabel"), "Information for Parcel:"))


        apn = driver.find_element_by_id("ParcelAPN")
        print(apn.text)

        all_data = {}
        all_data["apn"] = apn.text

        return all_data

      	


    except Exception as e:
        print(e)
        all_data = {}
        all_data["apn"] = "Something Went wrong"
        return all_data

    finally:
        pass
        driver.quit()



# print(perform_scraping_sacramento('4816 Emerson st'))


