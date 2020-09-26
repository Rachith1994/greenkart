

from selenium import webdriver

list0 = []
list2 = []
driver = webdriver.Chrome(executable_path="D:\python\chromedriver.exe")
driver.implicitly_wait(15)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(10)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
list1 = driver.find_elements_by_xpath("//div[@class='products']/div/h4")
for name in list1:
    list0.append(name.text)
print(list0)


buttons = (driver.find_elements_by_xpath("//div[@class='product-action']/button"))
for button in buttons:
    button.click()
driver.find_element_by_xpath("//div[@class='cart']/a/img").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div/button").click()

after = driver.find_elements_by_css_selector("p.product-name")
for vegis in after:
    list2.append(vegis.text)
print(list2)

assert list0 == list2
original = driver.find_element_by_css_selector("span.discountAmt").text
print(original)
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
time.sleep(5)
discount = driver.find_element_by_css_selector("span.discountAmt").text
print(discount)
assert int(original) > float(discount)

total = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for i in total:
    sum = sum + int(i.text)
print(sum)

carttotal = int(driver.find_element_by_css_selector("span.totAmt").text)
print(carttotal)
assert sum == carttotal



