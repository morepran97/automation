from behave import *
from selenium import webdriver 
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os

@step('I open google home page')
def step_impl(context):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver_path = os.getcwd() + r"\features\drivers\edge\msedgedriver.exe"
    service = Service(driver_path)
    context.driver = webdriver.Edge(service=service, options=options)
    
    context.driver.get('https://www.google.com/')


@step('I clicked on menu')
def step_impl(context):
    menu_button = context.driver.find_element(By.XPATH, '//a[@role="button"]')
    menu_button.click()
    

@step('I displayed names')
def step_impl3(context):
    iframe = context.driver.find_element(By.XPATH, '//iframe[@role="presentation"]')
    context.driver.switch_to.frame(iframe)
    menu_apps = context.driver.find_elements(By.XPATH, '//*[@data-text="Account"]/parent::a/parent::li/parent::ul/li')
    for i in range(len(menu_apps)):
        print(menu_apps[i].text)
