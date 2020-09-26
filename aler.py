from selenium import webdriver
rachith = "naik"
driver= webdriver.Chrome(executable_path="D:\python\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("input#name").send_keys(rachith)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
pallavi = alert.text
assert rachith in alert.text
alert.accept()



