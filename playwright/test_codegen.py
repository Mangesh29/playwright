import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name=" Add To Cart").nth(5).click()
    page.get_by_role("button", name="   Cart").click()
    page.get_by_role("button", name="Buy Now❯").click()
    page.get_by_role("textbox", name="Select Country").click()
    page.get_by_role("textbox", name="Select Country").fill("ind")
    page.get_by_role("button", name=" India").click()
    page.get_by_text("Place Order").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)