import copy
import shutil

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import RpaHandler
import os

path = "D:\FFOutput\屏幕录像"

from pykeyboard import PyKeyboard
from pymouse import PyMouse
import my_logger

logger = my_logger.get_logger()
logger.debug('this is a message')

current_date_time = ''

current_file_path = ''

run_info = {}


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
    data_list_copy = copy.deepcopy(data_list)
    flag = True
    for index, row in enumerate(data_list):
        logger.debug("当前处理的保单号:" + row + "-开始")
        # 开始录取
        k.press_key(k.function_keys[6])
        start = time.time()
        try:
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
            safe_number = row
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
            id_card = "91120116MA07145H0M"

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

            if str(row) == "21509211000021002533":
                raise Exception("执行错误")

        except Exception as e:
            logger.error(e)
            logger.error("当前处理的保单号:" + row + "-异常")
            flag = False
            raise Exception("执行错误")
        finally:
            end = time.time()
            logger.debug("耗时:" + str((end - start)))

            # 结束录屏
            k.press_key(k.function_keys[8])
            time.sleep(2)
            # 结束录屏
            k.press_key(k.function_keys[8])
            time.sleep(2)
            if flag:
                try:
                    ## 移动文件并改名字
                    path_file_list = os.listdir(path)
                    for i in path_file_list:
                        if os.path.isfile(os.path.join(path, i)):
                            file_path = os.path.join(path, i)
                            shutil.move(file_path, os.path.join(current_file_path, str(row) + ".mp4"))
                    data_list_copy.pop(0)
                    RpaHandler.write_json(data_list_copy)
                except Exception as e:
                    # 删除失败文件
                    file_list = os.listdir(path)
                    file_list = [i for i in file_list if i.startswith("格式工厂 屏幕录像")]
                    for i in file_list:
                        file_path = os.path.join(path, i)
                        logger.debug("删除失败的视频文件:" + file_path)
                        os.remove(file_path)
                    raise Exception("执行错误")

            else:
                # 删除失败文件
                file_list = os.listdir(path)
                file_list = [i for i in file_list if i.startswith("格式工厂 屏幕录像")]
                for i in file_list:
                    file_path = os.path.join(path, i)
                    logger.debug("删除失败的视频文件:" + file_path)
                    os.remove(file_path)
            logger.debug("当前处理的保单号:" + row + "-结束")
            flag = True


if __name__ == '__main__':
    current_date_time = (time.strftime("%Y_%m_%d %H_%M_%S", time.localtime()))
    current_file_path = os.path.join(path, current_date_time + "屏幕录像")
    os.mkdir(os.path.join(path, current_date_time + "屏幕录像"))
    try:
        logger.debug("项目启动时间:" + current_date_time)

        data_list = RpaHandler.readExcel()
        run(data_list)

        end_date_time = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    finally:
        logger.debug("项目结束时间:" + current_date_time)


