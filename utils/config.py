import os
from sauceclient import SauceClient

USERNAME = os.environ.get('SAUCE_USERNAME', "testuj")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "0029898f-54be-48b2-9166-9306282bef0c")
sauce = SauceClient(USERNAME, ACCESS_KEY)

USER = "testujpl2o2"
PASSWORD = "testuj88"

PROVIDER_USER = "damian-wiklina"
PROVIDER_PASSWORD = "TestujPL1"

PROVIDER_USER2 = "sprinterem-odreki"
PROVIDER_PASSWORD2 = "TestoojemyClick"

PROVIDER_USER3 = "BRUM-BRUM86"
PROVIDER_PASSWORD3 = "TestujPL1"

CHANGE_PASSWORD_USER = "testujpltlen"

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "firefox",
#              "version": "33"}]

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "internet explorer",
#              "version": "11"}]

browsers = [{"platform": "Windows 8.1",
             "browserName": "internet explorer",
             "version": "8"},
            {"platform": "Windows 8.1",
             "browserName": "firefox",
             "version": "35"}]

# browsers = [{"platform": "Windows 8.1",
#              "browserName": "chrome",
#              "version": "31"},
#             {"platform": "Windows 8.1",
#              "browserName": "internet explorer",
#              "version": "11"},
#             {"platform": "Windows 8.1",
#              "browserName": "firefox",
#              "version": "33"}]