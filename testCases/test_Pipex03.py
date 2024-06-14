import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Login_Page import Login_Class
from pageObjects.Leads_Page import Class_Leads
from utilities.Logger import Logging_Class
from utilities.readConfigFile import ReadconfigClass
class Test_pinx:

    log = Logging_Class.log_generator()
    Email = ReadconfigClass.getEmail()
    Password = ReadconfigClass.getPassword()
    def test_person_filter_001(self, setup):
        self.log.info("Testcase test_user_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.lp = Class_Leads(self.driver)
        self.driver.implicitly_wait(20)
        self.log.info("Click On login Link")
        self.log.info("Enter Email" + self.Email)
        self.lg.Enter_Email(self.Email)
        self.log.info("Enter Password" + self.Password)
        self.lg.Enter_Password(self.Password)
        self.log.info("Click Login Button")
        self.lg.Click_Login_Button()
        self.lp.Leads_Click()
        self.lp.Person_click()
        self.lp.Onwer_click()
        self.lp.Click_John()
        self.lp.Click_Apple()
        self.lp.Click_Leads_group()
        if self.driver.title=="Leads | Persons - Pipex":
            assert True
        else:
            assert False

        def test_person_filter_001(self, setup):
            self.log.info("Testcase test_user_login_002 is started")
            self.log.info("Opening browser")
            self.driver = setup
            self.lg = Login_Class(self.driver)
            self.lp = Class_Leads(self.driver)
            self.driver.implicitly_wait(20)
            self.log.info("Click On login Link")
            self.log.info("Enter Email" + self.Email)
            self.lg.Enter_Email(self.Email)
            self.log.info("Enter Password" + self.Password)
            self.lg.Enter_Password(self.Password)
            self.log.info("Click Login Button")
            self.lg.Click_Login_Button()


