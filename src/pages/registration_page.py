from selene import be, have, by, browser


class RegistrationPage:
    
    def __init__(self):
        self.first_name_input = browser.element("#firstName")
        self.last_name_input = browser.element("#lastName")
        self.email_input = browser.element("#userEmail")
        self.phone_number = browser.element("#userNumber")
        self.birth_date_input = browser.element("#dateOfBirthInput")
        self.subject_input = browser.element("#subjectsInput")
        self.upload_file_button = browser.element("#uploadPicture")
        self.current_address_input = browser.element("#currentAddress")
        self.state_list = browser.element("#state")
        self.city_list = browser.element("#city")
        self.submit_button = browser.element("#submit")
    
    @staticmethod
    def open_browser():
        browser.open("https://demoqa.com/automation-practice-form")
    
    @staticmethod
    def delete_banners():
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
    
    @staticmethod
    def get_gender_input(gender):
        return browser.element(
            by.xpath(f"//input[@value='{gender}']/ancestor::div[contains(@class, 'custom-control')]"))
    
    @staticmethod
    def get_hobbies_input(hobby):
        return browser.element(by.xpath(
            f"//label[@class='custom-control-label' and text()='{hobby}']"
            "/ancestor::div[contains(@class, 'custom-checkbox')]"))
    
    def fill_name(self, first_name):
        self.first_name_input.should(be.blank).type(first_name)
    
    def fill_surname(self, second_name):
        self.last_name_input.should(be.blank).type(second_name)
    
    def fill_email(self, email):
        self.email_input.should(be.blank).type(email)
    
    def choose_gender(self, gender):
        """
        :param gender: 'Male', 'Female' or 'Other'
        """
        self.get_gender_input(gender).click()
    
    def fill_phone_number(self, number):
        self.phone_number.type(number)
    
    def fill_date_as_text(self, date):
        self.birth_date_input.click()
        browser.execute_script("document.getElementById('dateOfBirthInput').value = '';")
        self.birth_date_input.set(value=date).press_enter()
    
    def fill_date_from_calendar(self, day, month, year):
        self.birth_date_input.click()
        browser.element(by.xpath("//select[@class = 'react-datepicker__year-select']")).click().element(
            by.xpath(f"//option[text() = '{year}']")
        ).click()
        browser.element(by.xpath("//select[@class = 'react-datepicker__month-select']")).click().element(
            by.xpath(f"//option[text() = '{month}']")).click()
        browser.element(
            by.xpath(f"//div[contains(@class, 'react-datepicker__day') and text() = '{day}']")).click()
    
    def fill_subject(self, subject):
        self.subject_input.type(subject).press_enter()
    
    def fill_hobbies(self, *hobbies):
        """

        :param hobbies: Sports, Reading or Music

        """
        for i in hobbies:
            self.get_hobbies_input(i).should(be.clickable).click()
    
    def upload_file(self, path):
        self.upload_file_button.type(path)
    
    def fill_current_address(self, address):
        self.current_address_input.type(address)
    
    def choose_state(self, option):
        self.state_list.click()
        browser.element(f"//div[contains(@id, 'react-select-3-option') and contains(text(), '{option}')]").click()
    
    def choose_city(self, option):
        self.city_list.click()
        browser.element(f"//div[contains(@id, 'react-select-4-option') and contains(text(), '{option}')]").click()
    
    @staticmethod
    def assert_user_data(param, expected_value):
        (browser.element(by.xpath(f"//table/tbody//td[text() = '{param}']/following-sibling::td"))
         .should(have.text(expected_value)))
