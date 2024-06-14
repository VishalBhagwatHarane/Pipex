from selenium.webdriver.common.by import By


class Login_Class:
    Text_Email_ID = (By.ID, "login_email")
    Text_Password_ID = (By.ID, "login_password")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='button']")
    Verify_Login_XPATH = (By.XPATH, "//div[@class='col-xl-8 mb-primary']//div[@class='card-header bg-transparent p-primary d-flex justify-content-between align-items-center']")
    # Login_Link_XPATH = (By.XPATH, "//div[@class='avatars-w-40']//img[@alt='image']")
    Menu_Button_XPATH = (By.XPATH, "//a[@id='profileDropdown']")
    Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()='Log out']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        # self.driver.find_element(*Login_Class.Text_Email_ID).clear()
        self.driver.find_element(*Login_Class.Text_Email_ID).send_keys(email)

    def Email_Clear(self):
        self.driver.find_element(*Login_Class.Text_Email_ID).clear()

    def Enter_Password(self, password):
        # self.driver.find_element(*Login_Class.Text_Email_ID).clear()
        self.driver.find_element(*Login_Class.Text_Password_ID).send_keys(password)

    def Password_Clear(self):
        self.driver.find_element(*Login_Class.Text_Email_ID).clear()


    def Click_Login_Button(self):
        self.driver.find_element(*Login_Class.Click_Login_Button_XPATH).click()

    def Verify_Login_Status(self):
        try:
            self.driver.find_element(*Login_Class.Verify_Login_XPATH)
            return "Pass"
        except:
            return "Fail"

    # def Login_Link(self):
    #     self.driver.find_element(*Login_Class.Login_Link_XPATH).click()

    def Click_Menu_Button(self):
        self.driver.find_element(*Login_Class.Menu_Button_XPATH).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*Login_Class.Logout_Button_XPATH).click()
