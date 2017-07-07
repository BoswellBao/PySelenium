import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def autogeneration_security_group():
    driver = webdriver.Ie("C:\\Program Files (x86)\\Internet Explorer\\IEDriverServer.exe")
    driver.maximize_window()

    driver.get("http://192.168.1.209")
    #登录
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").clear()
    time.sleep(1)
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_class_name("but").click()

    #进入警情列表
    driver.implicitly_wait(30)
    driver.find_element_by_id("actionAlarmManage").click()
    time.sleep(2)
    #点击保安管理
    driver.implicitly_wait(10)
    mouse = driver.find_element_by_id("bagl")
    mouse.click()
    #点击保安组管理
    driver.find_elements(by="class name", value="x-tab-strip-text")[1].click()
    for i in range(1,35):
    #点击增加
        driver.find_elements(by="tag name", value="button")[13].click()
        #激活保安组名填写框
        driver.find_element_by_id("name").send_keys("保安组" + str(i))
        # 激活保安组名填写框
        driver.find_element_by_id("description").send_keys("保安组" + str(i))
        #选定第一个小区
        driver.find_elements(by="class name", value="x-grid3-row-checker")[-1].click()
        #点击确定添加
        driver.find_elements(by="tag name", value="button")[-1].click()


if __name__ == "__main__":
    autogeneration_security_group()



