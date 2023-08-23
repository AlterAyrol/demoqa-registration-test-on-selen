import allure
from allure_commons.types import Severity

from demoqa_registration_test_on_selen.registration_form_page import RegistrationFormPage

url = '/automation-practice-form'
date_for_test = {
    'first_name': 'Ivan',
    'last_name': 'Ivanov',
    'email': 'asdfg@mail.ru',
    'mobile': '0123456789',
    'birth_month': 'January',
    'birth_year': '1988',
    'birth_day': '14',
    'subject': 'eng',
    'address': 'city One and street Two',
    'state': 'NCR',
    'city': 'Noida',
    'submitting_text': 'Thanks for submitting the form'
}


@allure.tag('registration')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "AlterAyrol")
@allure.epic('Тестирование вкладок в боковом меню')
@allure.feature('Раздел Practice Form')
@allure.story("Пользователь заполняет форму регистрации тестовыми данными. Указывает пол - мужской, хобби - чтение'")
def test_registration_form_in_mid_level_format():
    registration = RegistrationFormPage()
    registration.open_page(url)

    registration.first_name_input(date_for_test['first_name'])
    registration.last_name_input(date_for_test['last_name'])

    registration.email_input(date_for_test['email'])

    registration.male_select()

    registration.phone_number_input(date_for_test['mobile'])

    registration.birthday_calendar_open()
    registration.birthday_month_select(date_for_test['birth_month'])
    registration.birthday_year_select(date_for_test['birth_year'])
    registration.birthday_day_select(date_for_test['birth_day'])

    registration.subject_input(date_for_test['subject'])

    registration.hobby_reading_select()

    registration.picture_send()

    registration.address_input(date_for_test['address'])

    registration.state_select(date_for_test['state'])
    registration.city_select(date_for_test['city'])

    registration.form_submit()

    registration.assert_form_registration_text(date_for_test['submitting_text'])
    registration.assert_form_registration_table(date_for_test)
    registration.assert_male()
    registration.assert_hobby_reading()
