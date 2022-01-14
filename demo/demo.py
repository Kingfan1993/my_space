from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import RpaHandler

from pykeyboard import PyKeyboard
from pymouse import PyMouse


def run(data_list):
    # create capabilities
    capabilities = DesiredCapabilities.INTERNETEXPLORER

    # delete platform and version keys

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    # start an instance of IE
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # 键盘
    k = PyKeyboard()


    for index,row in enumerate(data_list):
        # 开始录取
        k.press_key(k.function_keys[6])

        start = time.time()
        if index == 0:
            driver.get("http://www.zking.com/inquiry/index.jhtml")
            driver.find_element_by_xpath("//p[text()='非车险']").click()
            driver.execute_script('window.scrollBy(0, 160)')

        time.sleep(1)
        driver.switch_to.frame("yjx")
        time.sleep(1)

        #
        ##driver.execute_script('document.getElementById("policyNo1").value="123";')

        # 保单号
        var1 = driver.find_element_by_id("policyNo1")
        var1.clear()
        var1.click()
        safe_number = row[0]
        var1.send_keys(safe_number)


        time.sleep(0.8)

        # 公司
        var2 = driver.find_element_by_id("insuredName1")
        var2.clear()
        var2.click()
        company_name = "上汽安吉商业保理有限公司"
        var2.send_keys(company_name)


        time.sleep(0.8)

        # 证件号
        var3 = driver.find_element_by_id("insuredIDNo")
        var3.clear()
        var3.click()
        id_card = row[1]

        var3.send_keys(id_card)
        time.sleep(0.8)

        # 验证码
        var4 = driver.find_element_by_id("authCode1")

        var4.click()

        time.sleep(5)
        driver.find_element_by_xpath("//a[@onclick='return FormFrmSubmit1();']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[contains(@onclick,'linkClick(')]").click()

        driver.find_element_by_id("policyNo1").clear()
        driver.find_element_by_id("insuredName1").clear()
        driver.find_element_by_id("insuredIDNo").clear()

        time.sleep(6)

        driver.switch_to.window(driver.window_handles[1])

        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        end = time.time()
        print("耗时:" + str((end - start)))
        # 结束录屏
        k.press_key(k.function_keys[8])
        time.sleep(2)




if __name__ == '__main__':
    data_list = RpaHandler.readExcel()
    run(data_list)
    RpaHandler.renameFile()

