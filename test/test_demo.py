import os.path
from selene import browser, have


def test_form_demo():
    browser.open('/automation-practice-form')

    # enter first name, last name and phone number
    browser.element('#firstName').click().type('Alexander')
    browser.element('#lastName').click().type('Pupkin')
    browser.element('#userEmail').click().type('Pupkin@gmail.com')

    # gender and phone number
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').click().type('79067777777')

    #Date of Birth
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="10"]').click()
    browser.element('.react-datepicker__day--010').click()

    '''
    или
    browser.element('#dateOfBirthInput').click().type('10 Nov 1990')
    '''

    # subjects and hobbies
    browser.element('#subjectsInput').type('Com').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-3]').click()

    # upload picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('../picture/pocita.jpg'))

    #scroll to down
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # address, state and city
    browser.element('#currentAddress').click().type(
        '914751, Оренбургская область, город Волоколамск, проезд Сталина, 09')
    browser.element('#state #react-select-3-input').type('Har').press_enter()
    browser.element('#city #react-select-4-input').type('Kar').press_enter()

    # data entry confirmation button
    browser.element('#submit').press_enter()

    # Thanks for submitting the form
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts('Student Name Alexander Pupkin', 'Student Email Pupkin@gmail.com',
                                                    'Gender Male', 'Mobile 7906777777',
                                                    'Date of Birth 10 November,1990',
                                                    'Subjects Computer Science', 'Hobbies Sports, Music',
                                                    'Picture pocita.jpg',
                                                    'Address 914751, Оренбургская область, город Волоколамск, проезд Сталина, 09',
                                                    'State and City Haryana Karnal'))
