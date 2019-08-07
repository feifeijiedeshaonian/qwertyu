from appium import webdriver
# from time import sleep
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'MKJNW18313006941'
desired_caps['platforVersion'] = '8.0.0'
desired_caps['appPackage'] = 'com.wondershare.drfone'
desired_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'
# desired_caps['noReset'] = 'True'
desired_caps['noReset'] = 'False'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)

driver.find_element_by_id("com.wondershare.drfone:id/btnBackup").click()
WebDriverWait(driver, 8).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()
WebDriverWait(driver, 10).until(lambda x:x.find_element_by_class_name('android.widget.LinearLayout'))
contexts = driver.contexts
print(contexts)
driver.switch_to.context("WEBVIEW_com.wondershare.drfone")
driver.find_element_by_id("email").send_keys("1747701685@qq.com")
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/button').click()
driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name("android.widget.ImageButton").click()