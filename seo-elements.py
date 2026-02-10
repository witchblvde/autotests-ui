from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://stage.ruscore.ru/")

    seo_title = page.title()
    expect(seo_title).to_have_text('Результаты и статистика матчей по футболу, хоккею, баскетболу, теннису и волейболу Ruscore (Рускор')
    print(seo_title)


    page.wait_for_timeout(5000)

