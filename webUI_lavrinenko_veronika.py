import selenium
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select



class Automization:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.usr_id = "txtUsername"
        self.usr_password_id = "txtPassword"
        self.link = 'https://opensource-demo.orangehrmlive.com/'
        self.driver.get(self.link)

    def setUserName(self, username):
        username_input = self.driver.find_element(By.ID, self.usr_id)
        self.filling(username_input, username)

    def setPassword(self, password):
        password_input = self.driver.find_element(By.ID, self.usr_password_id)
        self.filling(password_input, password)

    def button_click(self, button):
        self.driver.find_element(By.XPATH, button).click()

    def select_and_fill(self, field, data):
        selectfield = self.driver.find_element(By.XPATH, field)
        self.filling(selectfield, data)

    def filling(self, select, data):
        self.fill = select.clear()
        self.fill = select.send_keys(data)

    def delete_element(self, field):
        selectfield = self.driver.find_element(By.XPATH, field).get_attribute('href')
        value = selectfield[(selectfield.index('=') + 1)::]
        srt = "ohrmList_chkSelectRecord_"
        srt += str(value)
        self.driver.find_element(By.ID, srt).click()
        self.driver.find_element(By.XPATH, '//*[@id="btnDelete"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="dialogDeleteBtn"]').click()

    def check(self, changes):
        page = self.driver.find_element(By.XPATH, changes)
        assert page != None

    def check_deletion(self,changes):
        page = self.driver.find_elements(By.XPATH, changes)
        assert len(page) == 0

def main():
    autotest = Automization()

    autotest.setUserName('Admin')
    autotest.setPassword('admin123')
    time.sleep(2)

    autotest.button_click('//*[@id="btnLogin"]')
    autotest.button_click("/html/body/div[1]/div[2]/ul/li[1]/a/b")
    autotest.button_click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
    autotest.button_click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")
    autotest.button_click("/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]")
    autotest.select_and_fill('//*[@id="jobTitle_jobTitle"]', 'Barista')
    autotest.select_and_fill("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/textarea",
                      'Make a good coffee')
    autotest.select_and_fill("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/textarea",
                      'I can work only in the afternoon')
    time.sleep(2)
    autotest.button_click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")

    check_job = "//*[contains(text(), 'Barista')]"
    autotest.check(check_job)

    autotest.button_click("//*[contains(text(), 'Barista')]")
    autotest.button_click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")
    autotest.select_and_fill('//*[@id="jobTitle_jobTitle"]', 'Waiter')

    autotest.select_and_fill('//*[@id="jobTitle_jobDescription"]', 'Accepting orders and receiving payment')
    autotest.button_click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")

    changes_title = "//*[contains(text(), 'Waiter')]"
    autotest.check(changes_title)

    changes_descr = "//*[contains(text(), 'Accepting orders and receiving payment')]"
    autotest.check(changes_descr)

    time.sleep(2)
    autotest.delete_element("//*[contains(text(), 'Waiter')]")
    changes_title = ("//*[contains(text(), 'Waiter')]")
    autotest.check_deletion(changes_title)


if __name__=='__main__':
    main()

