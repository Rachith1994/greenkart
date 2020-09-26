from selenium import webdriver
from selenium.webdriver.support import expected_conditions



list = []
list2 = []
driver = webdriver.Chrome(executable_path="D:\python\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(15)
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
vege =driver.find_elements_by_css_selector("h4.product-name")
for i in vege:
    list.append(i.text)
print(list)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element_by_css_selector("img[src='./images/bag.png']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

vegis= driver.find_elements_by_css_selector("p.product-name")
for veg in vegis:
    list2.append(veg.text)
print(list2)
assert list==list2
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located)
print(driver.find_element_by_css_selector("span.promoInfo").text)


