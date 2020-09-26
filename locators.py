from selenium import webdriver
driver= webdriver.Chrome(executable_path="D:\python\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
checkbox[2].click()
radio = driver.find_elements_by_css_selector("input.radioButton")
radio[1].click()

driver.find_element_by_css_selector("input#name").send_keys("Rachith")
driver.find_element_by_css_selector("input#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()



















