from selene import browser, be, have
import os


def test_submit_practice_form():
    # Открываем страницу с формой
    browser.open('/automation-practice-form')

    # Заполняем основные поля
    browser.element('#firstName').should(be.blank).type('Иван')
    browser.element('#lastName').should(be.blank).type('Петров')
    browser.element('#userEmail').should(be.blank).type('ivan.petrov@example.com')

    # Выбираем пол (Male)
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    # Вводим номер телефона
    browser.element('#userNumber').should(be.blank).type('1234567890')

    # Выбираем дату рождения (15 May 1990)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element('.react-datepicker__day--015').click()

    # Выбираем предмет (Computer Science)
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    # Выбираем хобби (Sports)
    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()

    # Загружаем файл (предварительно создайте файл test.txt в папке с тестом)
    file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    browser.element('#uploadPicture').set_value(file_path)

    # Вводим адрес
    browser.element('#currentAddress').should(be.blank).type('ул. Примерная, 123')

    # Выбираем штат и город
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()  # NCR
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()  # Delhi

    # Отправляем форму
    browser.element('#submit').press_enter()

    # Проверяем результаты
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Иван Петров',
        'ivan.petrov@example.com',
        'Male',
        '1234567890',
        '15 May,1990',
        'Computer Science',
        'Sports',
        'test.txt',
        'ул. Примерная, 123',
        'NCR Delhi'
    ))