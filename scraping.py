from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
import usaddress
from selenium.webdriver.firefox.options import Options



def normalizeStreetSuffixes(inputValue):
        '''
        Use common abbreviations -> USPS standardized abbreviation to replace common street suffixes

        Obtains list from https://www.usps.com/send/official-abbreviations.htm
        '''

        try:
            usps_street_abbreviations = {'trpk': 'tpke', 'forges': 'frgs', 'bypas': 'byp', 'mnr': 'mnr', 'viaduct': 'via', 'mnt': 'mt',
            'lndng': 'lndg', 'vill': 'vlg', 'aly': 'Alley', 'mill': 'ml', 'pts': 'Point', 'centers': 'ctrs', 'row': 'row', 'cnter': 'ctr',
            'hrbor': 'hbr', 'tr': 'Trail', 'lndg': 'lndg', 'passage': 'psge', 'walks': 'Walk', 'frks': 'frks', 'crest': 'Crest', 'crst':'Crest', 'meadows': 'mdws',
            'freewy': 'Freeway', 'garden': 'gdn', 'bluffs': 'blfs', 'vlg': 'vlg', 'vly': 'vly', 'fall': 'fall', 'trk': 'trak', 'squares': 'Square',
            'trl': 'Trail', 'harbor': 'hbr', 'frry': 'fry', 'div': 'dv', 'straven': 'stra', 'cmp': 'cp', 'grdns': 'gdns', 'villg': 'vlg',
            'meadow': 'mdw', 'trails': 'Trail', 'streets': 'Street', 'prairie': 'pr', 'hts': 'hts', 'crescent': 'Crescent', 'pass': 'pass',
            'ter': 'Terrace', 'port': 'prt', 'bluf': 'blf', 'avnue': 'Avenue', 'lights': 'lgts', 'rpds': 'rpds', 'harbors': 'hbrs',
            'mews': 'mews', 'lodg': 'ldg', 'plz': 'Plaza', 'tracks': 'trak', 'path': 'Path', 'pkway': 'Parkway', 'gln': 'Glen',
            'bot': 'btm', 'drv': 'Drive', 'rdg': 'rdg', 'fwy': 'Freeway', 'hbr': 'hbr', 'via': 'via', 'divide': 'dv', 'inlt': 'inlt',
            'fords': 'frds', 'avenu': 'ave', 'vis': 'Vista', 'brk': 'brk', 'rivr': 'riv', 'oval': 'oval', 'gateway': 'gtwy',
            'stream': 'strm', 'bayoo': 'byu', 'msn': 'msn', 'knoll': 'knl', 'expressway': 'expy', 'sprng': 'spg',
            'flat': 'flt', 'holw': 'holw', 'grden': 'gdn', 'trail': 'Trail', 'jctns': 'jcts', 'rdgs': 'rdgs',
            'tunnel': 'tunl', 'ml': 'ml', 'fls': 'fls', 'flt': 'flt', 'lks': 'lks', 'mt': 'mt', 'groves': 'grvs',
            'vally': 'vly', 'ferry': 'fry', 'parkway': 'Parkway', 'radiel': 'radl', 'strvnue': 'stra', 'fld': 'fld',
            'overpass': 'opas', 'plaza': 'Plaza', 'estate': 'est', 'mntn': 'mtn', 'lock': 'lck', 'orchrd': 'orch',
            'strvn': 'stra', 'locks': 'lcks', 'bend': 'bnd', 'kys': 'kys', 'junctions': 'jcts', 'mountin': 'mtn',
            'burgs': 'bgs', 'pine': 'pne', 'ldge': 'ldg', 'causway': 'cswy', 'spg': 'spg', 'beach': 'bch', 'ft': 'ft',
            'crse': 'crse', 'motorway': 'mtwy', 'bluff': 'blf', 'court': 'Court', 'ct':'Court', 'grov': 'grv', 'sprngs': 'spgs',
            'ovl': 'oval', 'villag': 'vlg', 'vdct': 'via', 'neck': 'nck', 'orchard': 'orch', 'light': 'lgt',
            'sq': 'Square', 'pkwy': 'Parkway', 'shore': 'shr', 'green': 'grn', 'strm': 'strm', 'islnd': 'is',
            'turnpike': 'tpke', 'stra': 'stra', 'mission': 'msn', 'spngs': 'spgs', 'course': 'crse',
            'trafficway': 'trfy', 'terrace': 'Terrace', 'hway': 'Highway', 'avenue': 'ave', 'glen': 'Glen',
            'boul': 'Boulevard', 'blvd':'Boulevard', 'inlet': 'inlt', 'la': 'Lane', 'ln': 'Lane', 'frst': 'frst', 'clf': 'clf',
            'cres': 'Crescent', 'brook': 'brk', 'lk': 'lk', 'byp': 'byp', 'shoar': 'shr', 'bypass': 'byp',
            'mtin': 'mtn', 'ally': 'aly', 'forest': 'frst', 'junction': 'jct', 'views': 'vws', 'wells': 'wls', 'cen': 'ctr',
            'exts': 'exts', 'crt': 'ct', 'corners': 'cors', 'trak': 'trak', 'frway': 'Freeway', 'prarie': 'pr', 'crossing': 'xing',
            'extn': 'ext', 'cliffs': 'clfs', 'manors': 'mnrs', 'ports': 'prts', 'gatewy': 'gtwy', 'square': 'Square', 'hls': 'Hills',
            'harb': 'hbr', 'loops': 'Loop', 'mdw': 'mdw', 'smt': 'smt', 'rd': 'Road', 'hill': 'Hill', 'blf': 'blf',
            'highway': 'Highway', 'walk': 'Walk', 'clfs': 'clfs', 'brooks': 'brks', 'brnch': 'br', 'aven': 'ave',
            'shores': 'shrs', 'iss': 'iss', 'route': 'rte', 'wls': 'wls', 'place': 'Place', 'sumit': 'smt', 'pines': 'pnes',
            'trks': 'trak', 'shoal': 'shl', 'strt': 'Street', 'frwy': 'Freeway', 'heights': 'hts', 'ranches': 'rnch',
            'boulevard': 'Boulevard', 'extnsn': 'ext', 'mdws': 'mdws', 'hollows': 'holw', 'vsta': 'Vista', 'plains': 'plns',
            'station': 'sta', 'circl': 'Circle', 'mntns': 'mtns', 'prts': 'prts', 'shls': 'shls', 'villages': 'vlgs',
            'park': 'Park', 'nck': 'nck', 'rst': 'rst', 'haven': 'hvn', 'turnpk': 'tpke', 'expy': 'expy', 'sta': 'sta',
            'expr': 'expy', 'stn': 'sta', 'expw': 'expy', 'street': 'Street', 'str': 'Street', 'spurs': 'spur', 'crecent': 'Crescent',
            'rad': 'radl', 'ranch': 'rnch', 'well': 'wl', 'shoals': 'shls', 'alley': 'aly', 'plza': 'Plaza', 'medows': 'mdws',
            'allee': 'aly', 'knls': 'knls', 'ests': 'ests', 'st': 'Street', 'anx': 'anx', 'havn': 'hvn', 'paths': 'Path', 'bypa': 'byp',
            'spgs': 'spgs', 'mills': 'mls', 'parks': 'Park', 'byps': 'byp', 'flts': 'flts', 'tunnels': 'tunl', 'club': 'clb', 'sqrs': 'Square',
            'hllw': 'holw', 'manor': 'mnr', 'centre': 'ctr', 'track': 'trak', 'hgts': 'hts', 'rnch': 'rnch', 'crcle': 'cir', 'falls': 'fls',
            'landing': 'lndg', 'plaines': 'plns', 'viadct': 'via', 'gdns': 'gdns', 'gtwy': 'gtwy', 'grove': 'grv', 'camp': 'cp', 'tpk': 'tpke',
            'drive': 'Drive', 'freeway': 'Freeway', 'ext': 'ext', 'points': 'Point', 'exp': 'expy', 'ky': 'ky', 'courts': 'cts', 'pky': 'Parkway', 'corner': 'cor',
            'crssing': 'xing', 'mnrs': 'mnrs', 'unions': 'uns', 'cyn': 'cyn', 'lodge': 'ldg', 'trfy': 'trfy', 'circle': 'cir', 'bridge': 'brg',
            'dl': 'dl', 'dm': 'dm', 'express': 'expy', 'tunls': 'tunl', 'dv': 'dv', 'dr': 'Drive', 'shr': 'shr', 'knolls': 'knls', 'greens': 'grns',
            'tunel': 'tunl', 'fields': 'flds', 'common': 'Common', 'cmn' : 'Common', 'orch': 'orch', 'crk': 'crk', 'river': 'riv', 'shl': 'shl', 'view': 'vw',
            'crsent': 'Crescent', 'rnchs': 'rnch', 'crscnt': 'Crescent', 'arc': 'arc', 'btm': 'btm', 'blvd': 'blvd', 'ways': 'Way', 'radl': 'radl',
            'rdge': 'rdg', 'causeway': 'cswy', 'parkwy': 'Parkway', 'juncton': 'jct', 'statn': 'sta', 'gardn': 'gdn', 'mntain': 'mtn',
            'crssng': 'xing', 'rapid': 'rpd', 'key': 'ky', 'plns': 'plns', 'wy': 'Way', 'cor': 'cor', 'ramp': 'ramp', 'throughway': 'trwy',
            'estates': 'ests', 'ck': 'crk', 'loaf': 'lf', 'hvn': 'hvn', 'wall': 'wall', 'hollow': 'holw', 'canyon': 'cyn', 'clb': 'clb',
            'cswy': 'cswy', 'village': 'vlg', 'cr': 'crk', 'trce': 'trce', 'cp': 'cp', 'cv': 'cv', 'ct': 'cts', 'pr': 'pr', 'frg': 'frg',
            'jction': 'jct', 'pt': 'Point', 'mssn': 'msn', 'frk': 'frk', 'brdge': 'brg', 'cent': 'ctr', 'spur': 'spur', 'frt': 'ft', 'pk': 'Park',
            'fry': 'fry', 'pl': 'Place', 'lanes': 'Lane', 'gtway': 'gtwy', 'prk': 'Park', 'vws': 'vws', 'stravenue': 'stra', 'lgt': 'lgt',
            'hiway': 'Highway', 'ctr': 'ctr', 'prt': 'prt', 'ville': 'vl', 'plain': 'pln', 'mount': 'mt', 'mls': 'mls', 'loop': 'Loop',
            'riv': 'riv', 'centr': 'ctr', 'is': 'is', 'prr': 'pr', 'vl': 'vl', 'avn': 'ave', 'vw': 'vw', 'ave': 'ave', 'spng': 'spg',
            'hiwy': 'Highway', 'dam': 'dm', 'isle': 'isle', 'crcl': 'Circle', 'sqre': 'Square', 'jct': 'jct', 'jctn': 'jct', 'mountain': 'mtn',
            'keys': 'kys', 'parkways': 'Parkway', 'drives': 'Drive', 'drs' : 'Drive', 'tunl': 'tunl', 'jcts': 'jcts', 'knl': 'knl', 'center': 'ctr',
            'driv': 'Drive', 'tpke': 'tpke', 'sumitt': 'smt', 'canyn': 'cyn', 'ldg': 'ldg', 'harbr': 'hbr', 'rest': 'rst', 'shoars': 'shrs',
            'vist': 'Vista', 'gdn': 'gdn', 'islnds': 'iss', 'hills': 'Hills', 'cresent': 'Crescent', 'point': 'Point', 'lake': 'lk', 'vlly': 'vly',
            'strav': 'stra', 'crossroad': 'xrd', 'bnd': 'bnd', 'strave': 'stra', 'stravn': 'stra', 'knol': 'knl', 'vlgs': 'vlgs',
            'forge': 'frg', 'cntr': 'ctr', 'cape': 'cpe', 'height': 'hts', 'lck': 'lck', 'highwy': 'Highway', 'trnpk': 'tpke', 'rpd': 'rpd',
            'boulv': 'blvd', 'circles': 'Circle', 'valleys': 'vlys', 'vst': 'Vista', 'creek': 'crk', 'mall': 'Mall', 'spring': 'spg',
            'brg': 'brg', 'holws': 'holw', 'lf': 'lf', 'est': 'est', 'xing': 'xing', 'trace': 'trce', 'bottom': 'btm',
            'streme': 'strm', 'isles': 'isle', 'circ': 'Circle', 'forks': 'frks', 'burg': 'bg', 'run': 'run', 'trls': 'Trail',
            'radial': 'radl', 'lakes': 'lks', 'rue': 'rue', 'vlys': 'vlys', 'br': 'br', 'cors': 'cors', 'pln': 'pln',
            'pike': 'pike', 'extension': 'ext', 'island': 'is', 'frd': 'frd', 'lcks': 'lcks', 'terr': 'Terrace',
            'union': 'un', 'extensions': 'exts', 'pkwys': 'Parkway', 'islands': 'iss', 'road': 'Road', 'shrs': 'shrs',
            'roads': 'Road', 'glens': 'Glen', 'glns': 'Glen', 'springs': 'spgs', 'missn': 'msn', 'ridge': 'rdg', 'arcade': 'arc',
            'bayou': 'byu', 'crsnt': 'Crescent', 'junctn': 'jct', 'way': 'Way', 'valley': 'vly', 'fork': 'frk',
            'mountains': 'mtns', 'bottm': 'btm', 'forg': 'frg', 'ht': 'hts', 'ford': 'frd', 'hl': 'Hill',
            'grdn': 'gdn', 'fort': 'ft', 'traces': 'trce', 'cnyn': 'cyn', 'cir': 'Circle', 'un': 'un', 'mtn': 'mtn',
            'flats': 'flts', 'anex': 'anx', 'gatway': 'gtwy', 'rapids': 'rpds', 'villiage': 'vlg', 'flds': 'flds',
            'coves': 'Cove', 'rvr': 'riv', 'av': 'ave', 'pikes': 'pike', 'grv': 'grv', 'vista': 'Vista', 'pnes': 'pnes',
            'forests': 'frst', 'field': 'fld', 'branch': 'br', 'grn': 'grn', 'dale': 'dl', 'rds': 'Road', 'annex': 'anx',
            'sqr': 'Square', 'Cove': 'cv', 'cv':'Cove', 'cvs' : 'Cove', 'squ': 'Square', 'skyway': 'skwy', 'ridges': 'rdgs', 'hwy': 'Highway', 'tunnl': 'tunl',
            'underpass': 'upas', 'cliff': 'clf', 'lane': 'Lane', 'land': 'land', 'bch': 'bch', 'dvd': 'dv', 'curve': 'curv',
            'cpe': 'cpe', 'summit': 'smt', 'gardens': 'gdns', 'bay': 'Bay'}
        except Exception as e:
            print(e)
            return 0

        
        return usps_street_abbreviations[inputValue]




def perform_scraping(address_string, browser, headless, chrome_path, firefox_path):
    # options["executable_path"] = "/Users/apoorv/Hausable/selenium_scraping/chromedriver"
    # Create a new instance of the Firefox driver
    
    # # chrome_options = Options()
    # # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.binary_location = GOOGLE_CHROME_BIN
    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)


    #For scraping in Firefox

    if browser == "firefox":
        options = Options()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path = firefox_path, firefox_options=options)
    else:
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

    driver.get("https://www.acgov.org/MS/prop/index.aspx")


    # the page is ajaxy so the title is originally this:
    print(driver.title)


    # address_string='2313 Oregon St, Berkeley, CA'



    tagged_address = usaddress.tag(address_string)



    # street_name = "Oregon"
    # street_number = 2313
    # street_type = "Street"
    # city_name = "Berkeley"


    street_name = tagged_address[0]['StreetName']
    street_number = tagged_address[0]['AddressNumber']
    street_type_abbr = tagged_address[0]['StreetNamePostType'].replace(".", "").lower()
    street_type = normalizeStreetSuffixes(street_type_abbr)
    city_name = tagged_address[0]['PlaceName'].title()


    print("*"*10)

    print(street_name)
    print(street_number)
    print(street_type)
    print(city_name)


    wait = ui.WebDriverWait(driver,10)


    # # find the element that's name attribute is q (the google search box)
    # inputElement = driver.find_element_by_name("q")

    # # type in the search
    # inputElement.send_keys("cheese!")

    # # submit the form (although google automatically searches now without submitting)
    # inputElement.submit()

    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        # WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
        # pass

        

        txtStreetNum_inputElement = driver.find_element_by_id("txtStreetNum")
        txtStreetNum_inputElement.send_keys(str(street_number))

        txtStreetName_inputElement = driver.find_element_by_id("txtStreetName")
        txtStreetName_inputElement.send_keys(street_name)

        ddlbStreetType_inputElement = Select(driver.find_element_by_id('ddlbStreetType'))
        ddlbStreetType_inputElement.select_by_visible_text(street_type)

        ddlbCity_inputElement = Select(driver.find_element_by_id('ddlbCity'))
        ddlbCity_inputElement.select_by_visible_text(city_name)

        btnSubmit_inputElement = driver.find_element_by_id("btnSubmit")
        btnSubmit_inputElement.send_keys(Keys.ENTER)

        wait.until(lambda driver: driver.find_element_by_id('Import1'))

        print(driver.title)

        all_data = {}

        parcel_number = driver.find_element_by_id("FormView1_print_parcel_label").text
        use_code = driver.find_element_by_id("FormView1_Label2").text
        use_name = driver.find_element_by_id("FormView1_use_name_label").text
        description = driver.find_element_by_id("FormView1_use_name_label").text
        land = driver.find_element_by_id("FormView1_use_name_label").text
        improvements = driver.find_element_by_id("FormView1_roll_imps_label").text
        fixtures = driver.find_element_by_id("FormView1_roll_imps_label").text
        household_personal_property = driver.find_element_by_id("FormView1_roll_hpp_label").text
        business_personal_property = driver.find_element_by_id("FormView1_roll_bpp_label").text
        total_taxable_value = driver.find_element_by_id("FormView1_roll_tot_tax_label").text
        exemptions_homeowner = driver.find_element_by_id("FormView1_roll_hoex_label").text
        exceptions_other = driver.find_element_by_id("FormView1_roll_otex_label").text
        exceptions_total_net_taxable_other = driver.find_element_by_id("FormView1_roll_net_tax_label").text
        link_to_map = driver.find_element_by_id("FormView1_mapHyperLink").get_attribute('href')
        part1, part2 = link_to_map.split("(")
        part2 = part2[:-2]
        part2a = part2.split(",")[0][1:-1]

        all_data["parcel_number"] = parcel_number
        all_data["use_code"] = use_code
        all_data["use_name"] = use_name
        all_data["description"] = description
        all_data["land"] = land
        all_data["improvements"] = improvements
        all_data["fixtures"] = fixtures
        all_data["household_personal_property"] = household_personal_property
        all_data["business_personal_property"] = business_personal_property
        all_data["total_taxable_value"] = total_taxable_value
        all_data["exemptions_homeowner"] = exemptions_homeowner
        all_data["exceptions_other"] = exceptions_other
        all_data["exceptions_total_net_taxable_other"] = exceptions_total_net_taxable_other
        all_data["link_to_map"] = part2a



        print(parcel_number)
        print(use_code)
        print(use_name)
        print(description)
        print(land)
        print(improvements)
        print(fixtures)
        print(household_personal_property)
        print(business_personal_property)
        print(total_taxable_value)
        print(exemptions_homeowner)
        print(link_to_map)
        print(part2a)


        f = open("alameda.txt", "w")
        f.write( all_data  )      # str() converts to string
        f.close()

        return all_data




    except Exception as e:
    	print(e)

    finally:
        pass
        # driver.quit()






