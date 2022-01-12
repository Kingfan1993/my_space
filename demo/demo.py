from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

if __name__ == '__main__':
    # create capabilities
    capabilities = DesiredCapabilities.INTERNETEXPLORER

    # delete platform and version keys


    # start an instance of IE
    driver = webdriver.Chrome()

    driver.get("http://www.zking.com/inquiry/index.jhtml")

    driver.find_element_by_xpath("//p[text()='非车险']").click()
    time.sleep(1)
    driver.switch_to.frame("yjx")

    #
    driver.execute_script('document.getElementById("policyNo1").value="123";')
    driver.execute_script('document.getElementById("insuredName1").value="123";')
    driver.execute_script('document.getElementById("insuredIDNo").value="123";')
    driver.execute_script('document.getElementById("authCode1").value="123";')