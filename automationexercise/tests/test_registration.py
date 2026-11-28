import time

from pages.login_signup_page import LoginSignupPage
from pages.account_form_page import AccountFormPage
from pages.account_status_page import AccountStatusPage


def new_email():
    return f"qa.tester.{int(time.time())}@example.com"


def test_start_signup_opens_account_form(driver):
    page = LoginSignupPage(driver)
    page.open()
    page.start_signup("QA Tester", new_email())
    assert "/signup" in driver.current_url


def test_tc_reg_001_register_and_delete_account(driver):
    login_page = LoginSignupPage(driver)
    login_page.open()
    login_page.start_signup("QA Tester", new_email())

    form = AccountFormPage(driver)
    form.fill_account_details(
        password="Test1234!",
        first_name="QA",
        last_name="Tester",
        address="Test Street 123",
        country="Canada",
        state="Ontario",
        city="Toronto",
        zipcode="12345",
        mobile_number="3001234567",
    )
    form.submit()

    status = AccountStatusPage(driver)
    assert "account created" in status.get_created_message().lower()

    status.click_continue()
    status.delete_account()
    assert "account deleted" in status.get_deleted_message().lower()
