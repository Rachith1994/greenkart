from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:\python\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

rachith = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(rachith))

for i in rachith:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()

radio = driver.find_elements_by_class_name("radioButton")
radio[1].click()
assert radio[1].is_selected()
