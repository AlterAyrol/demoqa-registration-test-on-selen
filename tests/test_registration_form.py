import allure
from allure_commons.types import Severity

from demoqa_registration_test_on_selen.registration_form_page import RegistrationFormPage
from demoqa_registration_test_on_selen.data import date_for_registration_page


@allure.tag('registration')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование вкладок в боковом меню')
@allure.feature('Раздел Practice Form')
@allure.story("Пользователь заполняет форму регистрации тестовыми данными. Указывает пол - мужской, хобби - чтение'")
def test_registration_form_in_mid_level_format():
    user = date_for_registration_page.user_male_reading
    registration = RegistrationFormPage()

    registration.open_page()

    registration.first_name_input(user.first_name)
    registration.last_name_input(user.last_name)

    registration.email_input(user.email)

    registration.male_select()

    registration.phone_number_input(user.mobile)

    registration.birthday_calendar_open()
    registration.birthday_month_select(user.birth_month)
    registration.birthday_year_select(user.birth_year)
    registration.birthday_day_select(user.birth_day)

    registration.subject_input(user.subject)

    registration.hobby_reading_select()

    registration.picture_send()

    registration.address_input(user.address)

    registration.state_select(user.state)
    registration.city_select(user.city)

    registration.form_submit()

    registration.assert_form_registration_text(user.submitting_text)
    registration.assert_form_registration_table(user)
    registration.assert_male()
    registration.assert_hobby_reading()
