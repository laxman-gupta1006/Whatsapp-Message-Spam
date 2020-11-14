from selenium import webdriver
driver=webdriver.Chrome('chromedriver.exe')
driver.get('http://web.whatsapp.com')
name = input('Enter the name of user or group : ')
input('Enter anything after scanning QR code')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_elements_by_class_name('_3FRCZ')
for i in range(0,2000):
    msg_box[1].send_keys("Hi")
    driver.find_element_by_class_name('_1U1xa').click()