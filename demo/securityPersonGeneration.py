import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def autogeneration_security_person():
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

    # 进入保安管理
    actionAlarmManage = (By.ID, "actionAlarmManage")
    try:
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(actionAlarmManage))
    finally:
        driver.find_element_by_id("actionAlarmManage").click()
    time.sleep(1)
    #点击保安管理
    mouse = driver.find_element_by_id("bagl")
    mouse.click()
    time.sleep(1)

    phone = 18352861000
    for i in range(31):
        #把当前页面所有button放到列表，再从列表中找到要的那个button
        buttons = driver.find_elements(by="tag name", value="button")
        time.sleep(1)
        buttons[3].click()
        time.sleep(1)
        #填写新增信息
        driver.find_element_by_id("addName").send_keys("保安" + str(i))
        driver.find_element_by_id("addPhone").send_keys(phone)
        #把当前页面所有input放到列表，再从列表中找到要的那个input——保安组选择框
        inputs = driver.find_elements(by="tag name", value="input")
        inputs[15].click()
        inputs[15].send_keys(Keys.ENTER)
        #点击确定添加按钮
        but_classes = driver.find_elements(by="class name", value="x-btn-text")
        but_classes[-1].click()
        time.sleep(1)
        phone +=1


if __name__ == "__main__":
    autogeneration_security_person()



