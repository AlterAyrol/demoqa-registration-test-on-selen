from selene import browser
from selene import be, have
import os


class RegistrationFormPage:
    browser.config.base_url = 'https://demoqa.com'

    def __init__(self):
        self.browser = browser

    # Locators

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
    day_container_locator = '//div[@class="react-datepicker__day react-datepicker__day--0**"]'

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


    # Actions

    '''открытие нужной страницы'''
    def open_page(self, url: str):
        self.browser.open(url)

    '''Ввод имени с проверкой что поле пустое'''
    def first_name_input(self, first_name: str):
        browser.element(self.first_name_locator).should(be.blank).type(first_name)

    '''#Ввод фамилии с проверкой что поле пустое'''
    def last_name_input(self, last_name: str):
        browser.element(self.last_name_locator).should(be.blank).type(last_name)

    '''Ввод емейла с проверкой что поле пустое'''
    def email_input(self, email: str):
        browser.element(self.email_locator).should(be.blank).type(email)

    '''Выбор мужского пола'''
    def male_select(self):
        browser.element(self.gender_male_locator).click()

    '''Выбор женского пола'''
    def female_select(self):
        browser.element(self.gender_female_locator).click()

    '''Выбор промежуточного пола'''
    def other_select(self):
        browser.element(self.gender_other_locator).click()

    '''Ввод номера мобильного телефона с проверкой что поле пустое'''
    def phone_number_input(self, number: str):
        browser.element(self.mobile_locator).should(be.blank).type(number)

    '''Открытие календаря'''
    def birthday_calendar_open(self):
        browser.element(self.date_of_birth_locator).click()

    '''Выбор месяца рождения'''
    def birthday_month_select(self, month: str):
        browser.element(self.month_locator).type(month).press_enter()

    '''Выбор года рождения'''
    def birthday_year_select(self, year: str):
        browser.element(self.year_locator).type(year).press_enter()

    '''Выбор дня рождения'''
    def birthday_day_select(self, day: str):
        new_day_container_locator = self.day_container_locator.replace('**', day)
        browser.element(new_day_container_locator).click()

    '''Ввод тематики'''
    def subject_input(self, subject):
        browser.element(self.subjects_locator).click().type(subject).press_enter()

    '''Выбор хобби - спорт'''
    def hobby_sport_select(self):
        browser.element(self.hobbies_sports_locator).click()

    '''Выбор хобби - чтение'''
    def hobby_reading_select(self):
        browser.element(self.hobbies_reading_locator).click()

    '''Выбор хобби - музыка'''
    def hobby_music_select(self):
        browser.element(self.hobbies_music_locator).click()

    '''Отправка картинки'''
    def picture_send(self):
        browser.element(self.picture_locator).send_keys(os.path.abspath('../resources/for_send.bmp'))

    '''Ввод адреса с проверкой что поле пустое'''
    def address_input(self, address):
        browser.element(self.address_locator).should(be.blank).type(address)

    '''Выбор штата'''
    def state_select(self, state):
        browser.element(self.select_state_locator).type(state).press_enter()

    '''Выбор города'''
    def city_select(self, city):
        browser.element(self.select_city_locator).type(city).press_enter()

    '''Подтверждение отправки формы'''
    def form_submit(self):
        browser.element(self.submit_button_locator).click()


