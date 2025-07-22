from selene import browser, be, have
import os

def test_submit_practice_form():
    file_path = os.path.join(os.path.dirname(__file__), 'testfile.txt')
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Петр')
    browser.element('#lastName').should(be.blank).type('Петров')
    browser.element('#userEmail').should(be.blank).type('petr.petrov@example.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1985')
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('.custom-checkbox').element_by(have.exact_text('Waha')).click()
    browser.element('#uploadPicture').send_keys(file_path)
    browser.element('#currentAddress').type('ул. Тестовая, 007')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').press_enter()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Иван Петров',
        'ivan.petrov@example.com',
        'Male',
        '1234567890',
        '15 May,1990',
        'Computer Science',
        'Sports',
        'testfile.txt',
        'ул. Примерная, 123',
        'NCR Delhi'
    ))