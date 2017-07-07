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
    time.sleep(10)
    driver.find_element_by_id("actionAlarmManage").click()
    time.sleep(5)
    #鼠标悬停在警情上
    mouse = driver.find_element_by_id("actionAlarmManage")
    ActionChains(driver).move_to_element(mouse)
    time.sleep(2)
    #点击保安管理
    #driver.find_elements_by_class_name("glyphicon glyphicon-retweet")[3].click()  #(by="class name", value="glyphicon glyphicon-retweet")[3].click()
    driver.find_element_by_id("bagl").click()
    #点击保安组管理
    driver.find_elements(by="class name", value="x-tab-strip-text")[2].click()
    #点击增加
    driver.find_elements(by="class name", value="x-btn-text")[9].click()
    #激活保安组名填写框
    driver.find_element_by_id("name").send_keys("保安组1")
    # 激活保安组名填写框
    driver.find_element_by_id("description").send_keys("保安组1")
    #选定第一个小区
    driver.find_elements(by="class name", value="x-grid3-cell-inner x-grid3-col-name")[1].click()
    #点击确定添加
    driver.find_elements(by="class name", value="x-btn-text")[13].click()

    # time.sleep(1)
    # nameid = 1
    # phone = 18352861000
    # for i in range(31):
    #     #把当前页面所有button放到列表，再从列表中找到要的那个button
    #     buttons = driver.find_elements(by="tag name", value="button")
    #     time.sleep(1)
    #     buttons[3].click()
    #     time.sleep(1)
    #     #填写新增信息
    #     driver.find_element_by_id("addName").send_keys("保安" + str(nameid))
    #     driver.find_element_by_id("addPhone").send_keys(phone)
    #     #把当前页面所有input放到列表，再从列表中找到要的那个input——保安组选择框
    #     inputs = driver.find_elements(by="tag name", value="input")
    #     inputs[15].click()
    #     inputs[15].send_keys(Keys.ENTER)
    #     #点击确定添加按钮
    #     but_classes = driver.find_elements(by="class name", value="x-btn-text")
    #     but_classes[-1].click()
    #     time.sleep(1)
    #     nameid += 1
    #     phone +=1


if __name__ == "__main__":
    autogeneration_security_group()



