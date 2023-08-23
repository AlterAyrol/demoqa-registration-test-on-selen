from selene import browser
from selene import be, have
import os

# data
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


#locators
first_name_locator = '//input[@id="firstName"]'
last_name_locator = '//input[@id="lastName"]'
email_locator = '//input[@id="userEmail"]'

gender_male_locator = '//label[@for="gender-radio-1"]'
gender_female_locator = '//label[@for="gender-radio-2"]'
gender_other_locator = '//label[@for="gender-radio-3"]'

mobile_locator = '//input[@id="userNumber"]'

date_of_birth_locator = '//input[@id="dateOfBirthInput"]'
month_locator = '//select[@class="react-datepicker__month-select"]'
year_locator = '//select[@class="react-datepicker__year-select"]'
day_container_locator = f'//div[@class="react-datepicker__day react-datepicker__day--0{birth_day}"]'

subjects_locator = '//input[@id="subjectsInput"]'

hobbies_sports_locator = '//label[@for="hobbies-checkbox-1""]'
hobbies_reading_locator = '//label[@for="hobbies-checkbox-2"]'
hobbies_music_locator = '//label[@for="hobbies-checkbox-3"]'

picture_locator = '//input[@id="uploadPicture"]'
address_locator = '//textarea[@id="currentAddress"]'

select_state_locator = '//input[@id="react-select-3-input"]'
select_city_locator = '//input[@id="react-select-4-input"]'

submit_button_locator = '//button[@id="submit"]'
submitting_form_locator = '//div[@id="example-modal-sizes-title-lg"]'
table_submitting_locator = '//div[@class="table-responsive"]//tbody'


def test_5():


    #открытие нужной страницы
    browser.open('/automation-practice-form')

    #Ввод имени и фамилии
    browser.element(first_name_locator).should(be.blank).type(first_name)
    browser.element(last_name_locator).should(be.blank).type(last_name)

    #Ввод емейла
    browser.element(email_locator).should(be.blank).type(email)

    #Выбор пола
    browser.element(gender_male_locator).click()

    #Ввод номера мобильного телефона
    browser.element(mobile_locator).should(be.blank).type(mobile)

    #Открытие календаря и выбор даты рождения
    browser.element(date_of_birth_locator).click()
    browser.element(month_locator).type(birth_month).press_enter()
    browser.element(year_locator).type(birth_year).press_enter()
    browser.element(day_container_locator).click()

    # Ввод тематики
    browser.element(subjects_locator).click().type(subject).press_enter()

    # Выбор хобби - чтение
    browser.element(hobbies_reading_locator).click()

    #Отправка картинки
    # browser.element(picture_locator).send_keys(os.path.abspath('../resources/for_send.bmp'))

    #Ввод адреса
    browser.element(address_locator).should(be.blank).type(address)

    #Выбор штата и города
    browser.element(select_state_locator).type(state).press_enter()
    browser.element(select_city_locator).type(city).press_enter()

    #Подтверждение формы
    browser.element(submit_button_locator).click()

    #Проверка на наличие формы подтверждения регистрации
    browser.element(submitting_form_locator).should(have.text(submitting_text))

    # Проверка данных в таблице
    browser.element(table_submitting_locator).should(have.text(f'{first_name} {last_name}'))
    browser.element(table_submitting_locator).should(have.text(email))
    browser.element(table_submitting_locator).should(have.text('Male'))
    browser.element(table_submitting_locator).should(have.text(mobile))
    browser.element(table_submitting_locator).should(have.text('14 January,1988'))
    browser.element(table_submitting_locator).should(have.text('Reading'))
    browser.element(table_submitting_locator).should(have.text('for_send.bmp'))
    browser.element(table_submitting_locator).should(have.text(address))
    browser.element(table_submitting_locator).should(have.text(f'{state} {city}'))
