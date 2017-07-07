import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def autogeneration_time_templet():
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
    #点击时间模板
    driver.implicitly_wait(10)
    mouse = driver.find_element_by_id("timeTemplate")
    mouse.click()
    time.sleep(1)
    for i in range(7,41):
        time.sleep(1)
        #点击增加
        driver.find_elements(by="tag name", value="button")[2].click()
        #激活时间模板名填写框并填写时间模板名
        time_templet_input_mouse = driver.find_elements(by="class name", value="x-form-element")[1]
        time_templet_input_mouse.click()
        time_templet_input_mouse.send_keys("时间模板" + str(i))
        # 点击第一行开始时间框并填写时间
        beginTime1_mouse = driver.find_element_by_id("beginTime1")
        beginTime1_mouse.click()
        beginTime1_mouse.send_keys(Keys.ENTER)
        time.sleep(1)
        #点击第一行结束时间框并填写时间
        endTime1_mouse = driver.find_element_by_id("endTime1")
        endTime1_mouse.click()
        endTime1_mouse.send_keys(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(2)
        #点击确定按钮
        driver.find_elements(by="tag name", value="button")[-2].click()


if __name__ == "__main__":
    autogeneration_time_templet()



