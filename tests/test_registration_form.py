from demoqa_registration_test_on_selen.registration_form_page import RegistrationFormPage

url = '/automation-practice-form'
first_name = 'Ivan'
last_name = 'Ivanov'
email = 'asdfg@mail.ru'
mobile = '0123456789'
birth_month = 'jan'
birth_year = '1988'
birth_day = '14'
subject = 'eng'
address = 'city One and street Two'
state = 'NCR'
city = 'Noida'
submitting_text = 'Thanks for submitting the form'


def test_registration_form_in_mid_level_format():
    registration = RegistrationFormPage()
    registration.open_page(url)

    registration.first_name_input(first_name)
    registration.last_name_input(last_name)

    registration.email_input(email)

    registration.male_select()

    registration.phone_number_input(mobile)

    registration.birthday_calendar_open()
    registration.birthday_month_select(birth_month)
    registration.birthday_year_select(birth_year)
    registration.birthday_day_select(birth_day)

    registration.subject_input(subject)

    registration.hobby_reading_select()

    registration.picture_send()

    registration.address_input(address)

    registration.state_select(state)
    registration.city_select(city)

    registration.form_submit()

