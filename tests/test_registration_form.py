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
def test_registration_form_in_high_level_format():
    registration = RegistrationFormPage()
    user = date_for_registration_page.user_male_reading

    registration.open_page()

    registration.fill_registration_form(user)

    registration.assert_full_registration_form(user)




