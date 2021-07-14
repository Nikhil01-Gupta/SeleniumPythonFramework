import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Non_Commerce.utilities.BaseClass import BaseClass


def month_select(sp):
    months = driver.find_elements_by_xpath("//table[@role='grid']//tr//a")
    Month_List = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for month in months:
        mn = month.text
        num = sp[1]
        conv_int = int(num)
        Get_Month = Month_List[conv_int - 1]
        if mn == Get_Month:
            month.click()
            break

def selectdate(date):
    driver.find_element_by_xpath("(//span[@class='k-icon k-i-calendar'])[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").click()
    time.sleep(2)
    year=driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").text
    sp = date.split("/")
    yy = sp[2]
    if yy == year:
        month_select(sp)

    else:
        while yy < year:
            driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[1]").click()
            year = driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").text
        while yy > year:
            driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[3]").click()
            year = driver.find_element_by_xpath("(//div[@id='AvailableStartDateTimeUtc_dateview']//a)[2]").text
        month_select(sp)

    dates = driver.find_elements_by_xpath("//table[@class='k-content k-month']//a")
    for dd in dates:
        dates = dd.text
        if dates == sp[0]:
            dd.click()
            break











def get_PageBottom_Scroll():
    sample = driver.find_element_by_tag_name("html")
    return sample.send_keys(Keys.END)


driver = webdriver.Chrome(executable_path=r"D:\chrome_setup\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com")
driver.maximize_window()
time.sleep(3)
#driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
#driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.find_element_by_link_text("Catalog").click()
time.sleep(3)
driver.find_element_by_xpath("//li[@class='nav-item has-treeview menu-open']//p[text()=' Products']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()
time.sleep(5)
read_more=driver.find_element_by_xpath("//label[contains(text(),'Require other products') and @for='RequireOtherProducts']")
driver.execute_script("arguments[0].scrollIntoView();", read_more)
date="14/07/2010"
selectdate(date)





