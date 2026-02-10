from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('test@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('test')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state-homework.json')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state-homework.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    #Наличие и текст заголовка "Courses"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_enabled()
    expect(courses_title).to_have_text('Courses')

    #Наличие и видимость иконки пустого блока
    courses_empty_list_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_list_icon).to_be_enabled()
    expect(courses_empty_list_icon).to_be_visible()

    #Наличие и текст блока "There is no results"
    courses_empty_list_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_list_text).to_be_enabled()
    expect(courses_empty_list_text).to_have_text('There is no results')

    #Наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    courses_empty_list_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_list_description).to_be_enabled()
    expect(courses_empty_list_description).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)


