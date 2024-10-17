from config import *

from src.pages.registration_page import RegistrationPage


def test_fill_form(setup_browser):
    registration_page = RegistrationPage()
    registration_page.open_browser()
    registration_page.delete_banners()
    registration_page.fill_name(name)
    registration_page.fill_surname(surname)
    registration_page.fill_email(test_email)
    registration_page.choose_gender(male_gender)
    registration_page.fill_phone_number(test_number)
    registration_page.fill_date_from_calendar(test_day, test_month, test_year)
    registration_page.fill_subject(test_subject)
    registration_page.fill_hobbies(sport_hobby, music_hobby)
    registration_page.upload_file(test_file)
    registration_page.fill_current_address(test_address)
    registration_page.choose_state(test_state)
    registration_page.choose_city(test_city)
    registration_page.submit_button.click()
    registration_page.assert_user_data("Student Name", f"{name} {surname}")
    registration_page.assert_user_data("Student Email", test_email)
    registration_page.assert_user_data("Gender", male_gender)
    registration_page.assert_user_data("Mobile", test_number)
    registration_page.assert_user_data("Date of Birth", f"{test_day} {test_month},{test_year}")
    registration_page.assert_user_data("Subjects", test_subject)
    registration_page.assert_user_data("Hobbies", f"{sport_hobby}, {music_hobby}")
    registration_page.assert_user_data("Picture", test_file.split("\\")[-1])
    registration_page.assert_user_data("Address", test_address)
    registration_page.assert_user_data("State and City", f"{test_state} {test_city}")
