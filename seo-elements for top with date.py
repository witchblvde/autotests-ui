from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://stage.ruscore.ru/2026-02-02", wait_until='domcontentloaded')

    desc = page.locator('').text_content()

    print(desc)



    page.wait_for_timeout(1000)

