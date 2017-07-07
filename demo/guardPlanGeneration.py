import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def autogeneration_guard_plan():
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

    #进入告警
    driver.implicitly_wait(30)
    driver.find_element_by_id("alarm").click()
    #点击布防计划
    driver.implicitly_wait(10)
    mouse = driver.find_element_by_id("bfjh")
    mouse.click()
    time.sleep(1)

    time.sleep(1)
    #点击增加
    driver.find_elements(by="tag name", value="button")[2].click()
    #填写计划名称
    driver.find_element_by_id("depName").send_keys("布防计划调试")
    #选择时间模板
    combobox = driver.find_element_by_id("ComboBox")
    combobox.click()
    combobox.send_keys(Keys.ARROW_DOWN * 5)
    combobox.send_keys(Keys.ENTER)
    #选择告警类型
    alarmType = driver.find_element_by_id("alarmType")
    alarmType.click()
    alarmType.send_keys(Keys.ARROW_DOWN * 3)
    alarmType.send_keys(Keys.ENTER)
    #填写描述
    driver.find_element_by_id("miaoshu").send_keys("布防计划调试")
    #选择设备
    driver.find_elements(by="class name", value="x-grid3-row-checker")[-1].click()
    #点击确定
    driver.find_elements(by="class name", value="x-btn-center")[-2].click()


if __name__ == "__main__":
    autogeneration_guard_plan()



