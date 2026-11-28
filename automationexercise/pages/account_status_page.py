from selenium.webdriver.common.by import By


class AccountStatusPage:
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "[data-qa='account-created']")    
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")    
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/delete_account']")  
    ACCOUNT_DELETED = (By.CSS_SELECTOR, "[data-qa='account-deleted']")    

    def __init__(self, driver):
        self.driver = driver

    def get_created_message(self):
        return self.driver.find_element(*self.ACCOUNT_CREATED).text

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def delete_account(self):
        self.driver.find_element(*self.DELETE_ACCOUNT_LINK).click()

    def get_deleted_message(self):
        return self.driver.find_element(*self.ACCOUNT_DELETED).text
