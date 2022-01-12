from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    # create capabilities
    capabilities = DesiredCapabilities.INTERNETEXPLORER

    # delete platform and version keys

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    # start an instance of IE
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("http://www.zking.com/inquiry/index.jhtml")

    driver.find_element_by_xpath("//p[text()='非车险']").click()
    time.sleep(1)
    driver.switch_to.frame("yjx")

    #
    ##driver.execute_script('document.getElementById("policyNo1").value="123";')

    # 保单号
    var1 = driver.find_element_by_id("policyNo1")
    var1.click()
    safe_number = "21509211000021002531"
    for i in safe_number:
        time.sleep(0.1)
        var1.send_keys(i)

    # 公司
    var2 = driver.find_element_by_id("insuredName1")
    var2.click()
    company_name = "上汽安吉商业保理有限公司"
    for i in company_name:
        time.sleep(0.1)
        var2.send_keys(i)

    # 证件号
    var3 = driver.find_element_by_id("insuredIDNo")
    var3.click()
    id_card = "91120116MA07145H0M"
    for i in id_card:
        time.sleep(0.1)
        var3.send_keys(i)

    # 验证码
    var4 = driver.find_element_by_id("authCode1")
    var4.click()

    time.sleep(5)
    driver.find_element_by_xpath("//a[@onclick='return FormFrmSubmit1();']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[contains(@onclick,'linkClick(')]").click()


