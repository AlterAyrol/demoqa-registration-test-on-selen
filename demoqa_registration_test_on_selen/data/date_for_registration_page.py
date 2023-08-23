from dataclasses import dataclass


@dataclass
class DateForRegistrationPage:
    first_name: str
    last_name: str
    email: str
    mobile: str
    birth_month: str
    birth_year: str
    birth_day: str
    subject: str
    address: str
    state: str
    city: str
    submitting_text: str


@dataclass
class UserWithGenderAndHobby(DateForRegistrationPage):
    gender: str
    hobby: str


user_male_reading = UserWithGenderAndHobby(
    first_name='Ivan',
    last_name='Ivanov',
    email='asdfg@mail.ru',
    mobile='0123456789',
    birth_month='January',
    birth_year='1988',
    birth_day='14',
    subject='eng',
    address='city One and street Two',
    state='NCR',
    city='Noida',
    submitting_text='Thanks for submitting the form',
    gender='Male',
    hobby='Reading'
)
