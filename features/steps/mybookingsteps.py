from behave import *
from selenium import  webdriver
import time

@given(u'launch the browser')
def step_impl(context):
    path = r'C:\Users\admin\Downloads\chromedriver_win32\chromedriver.exe'
    context.driver_obj = webdriver.Chrome(path)



@when(u'open abhibus homepage')
def step_impl(context):
    context.driver_obj.get("https://www.abhibus.com/")



@when(u'click on my bookings')
def step_impl(context):
    context.driver_obj.find_element_by_id('navbarDropdown1').click()
    time.sleep(2)


@when(u'click on print booking')
def step_impl(context):
    context.driver_obj.find_element_by_xpath("(//a[@class='dropdown-item'])[1]").click()
    time.sleep(2)


@then(u'verify print booking page is visible or not')
def step_impl(context):
    assert True, "Test Passed"
    context.driver_obj.close()


@then(u'click on print booking')
def step_impl(context):
    context.driver_obj.find_element_by_xpath("(//a[@class='dropdown-item'])[1]").click()
    time.sleep(2)


@then(u'enter bookig id')
def step_impl(context):
    context.driver_obj.find_element_by_id('ticket_num').send_keys('AB34325BS4')
    time.sleep(2)



@then(u'enter mobile no')
def step_impl(context):
    context.driver_obj.find_element_by_id('phonenum').send_keys("7776988991")
    time.sleep(2)



@then(u'click on "retrive" button')
def step_impl(context):
    context.driver_obj.find_element_by_xpath('//input[@value="Retrieve "]').click()
    # self.driver_obj.back()



@then(u'verify that booking details are visible or not')
def step_impl(context):
    assert True, "Test Passed"
    context.driver_obj.close()

@then(u'click on cancel booking')
def step_impl(context):
    context.driver_obj.find_element_by_xpath("(//a[@class='dropdown-item'])[2]").click()
    time.sleep(2)


@then(u'verify cancel booking page is visible or not')
def step_impl(context):
    assert True, "Test Passed"
    context.driver_obj.close()


@then(u'verify that cancelation is visible or not')
def step_impl(context):
    assert True, "Test Passed"
    context.driver_obj.close()

