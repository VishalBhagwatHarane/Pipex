from selenium.webdriver.common.by import By


class Class_Leads:
    Text_Leads_Click=(By.XPATH,"//a[@href='#leads']")
    Text_PERSON_Click=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/nav[2]/ul[1]/li[2]/div[1]/ul[1]/li[1]/a[1]")
    Text_Onwer_Click=(By.XPATH,"//button[@id='owner_is-person-modal']")
    Text_john_Click=(By.XPATH,"//label[normalize-space()='John Doe']")
    Text_Apple_Click=(By.XPATH,"//div[@class='dropdown-menu show']//button[@type='submit'][normalize-space()='Apply']")
    Text_lead_group=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/button[1]")


    def __init__(self,driver):
        self.driver=driver

    def Leads_Click(self):
        self.driver.find_element(*Class_Leads.Text_Leads_Click).click()

    def Person_click(self):
        self.driver.find_element(*Class_Leads.Text_PERSON_Click).click()

    def Onwer_click(self):
        self.driver.find_element(*Class_Leads.Text_Onwer_Click).click()

    def Click_John(self):
        self.driver.find_element(*Class_Leads.Text_john_Click).click()

    def Click_Apple(self):
        self.driver.find_element(*Class_Leads.Text_Apple_Click).click()

    def Click_Leads_group(self):
        self.driver.find_element(*Class_Leads.Text_lead_group).click()
