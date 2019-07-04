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





def perform_scraping_la(address_string, browser, headless, chrome_path, firefox_path):
    # options["executable_path"] = "/Users/apoorv/Hausable/selenium_scraping/chromedriver"
    # Create a new instance of the Firefox driver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options = Options()
    # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    # For Scraping in local
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/la/chromedriver")
    # browser = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe"))

    # go to the google home page

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


    # # # # For Scraping in local
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = "/Users/apoorv/Hausable/selenium_scraping/app/chromedriver", desired_capabilities=capabilities)




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

    driver.get("http://maps.assessor.lacounty.gov/GVH_2_2/Index.html?configBase=http://maps.assessor.lacounty.gov/Geocortex/Essentials/REST/sites/PAIS/viewers/PAIS_hv/virtualdirectory/Resources/Config/Default")


    # the page is ajaxy so the title is originally this:
    print(driver.title)


    # address_string='3836 hayvenhurst ave'



    # street_name = "Hayvenhurst"
    # street_number = 3836
    # street_type = "Avenue"
    # city_name = "Los Angeles"



    print("*"*10)


    wait = ui.WebDriverWait(driver,10)

    WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.CLASS_NAME,"home-panel-search-option-label")))

    title = driver.find_element_by_class_name("home-panel-search-option-label").text
    print(title)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@_key ='1']")))

    enter_address_text = driver.find_element_by_xpath("//a[@_key ='1']").text
    print(enter_address_text)

    enter_address = driver.find_element_by_xpath("//a[@_key ='1']")
    enter_address.click()

    wait = ui.WebDriverWait(driver,10)

    WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.CLASS_NAME,"addresssearch-field-input")))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txt_address")))

    address_bar = driver.find_element_by_id("txt_address");
    address_bar.send_keys(address_string);

    address_submit = driver.find_element_by_id("btn_SearchByAddress");
    address_submit.click();


    # # find the element that's name attribute is q (the google search box)
    # inputElement = driver.find_element_by_name("q")

    # # type in the search
    # inputElement.send_keys("cheese!")

    # # submit the form (although google automatically searches now without submitting)
    # inputElement.submit()

    driver.implicitly_wait(10)

    WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH,"//a[@_key ='4']")))


    parcel = driver.find_element_by_xpath("//a[@_key ='4']")
    parcel.click()


    

    parcel_1 = driver.find_element_by_xpath("//div[@class ='list-menu-details']")
    print(parcel_1.text)

    # parceldetails-module-view-section-body



    WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH,"//div[@class = 'parceldetails-attribute-label']")))
    WebDriverWait(driver, 100).until( EC.presence_of_element_located((By.XPATH,"//a[@href = 'https://vcheck.ttc.lacounty.gov/index.php']")))


    details = driver.find_elements_by_xpath("//div[@class = 'parceldetails-attribute-label']")
    # script = "return document.getElementsByClassName('parceldetails-attribute-label').innerHTML";
    for i in details:
        # print(i)
        # print(i.get_property('attributes'))
        print(i.text)

    data = []
    details = driver.find_elements_by_xpath("//div[@class = 'parceldetails-attribute-value']")
    # script = "return document.getElementsByClassName('parceldetails-attribute-label').innerHTML";
    for i in details:
        # print(i)
        # print(i.get_property('attributes'))
        print(i.text)
        data.append(i.text)


    test = driver.find_element_by_xpath("//div[@class = 'parceldetails-module-view-section-row']")
    print(test.text)

    return data



    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
        # pass

        # title = driver.find_element_by_class_name("panel-title")
        # print(title)
        pass

      	


    except Exception as e:
        print(e)

    finally:
        pass
        # driver.quit()



# perform_scraping_la('3836 hayvenhurst ave')


