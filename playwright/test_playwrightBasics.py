from playwright.sync_api import Page ,Playwright,expect
 
import time


def test_playwright_basics(playwright):   # golbal fixture playwright, page
    browser = playwright.chromium.launch(headless=False) # Launch browser
    context = browser.new_context() # Create a new browser context
    page=context.new_page() # Open a new page
    page.goto("https://rahulshettyacademy.com") # Navigate to URl

    #chromium headless mode , 1 singal
def test_playwight_shortcut(page:Page):  # Using page fixture directly
    page.goto("https://rahulshettyacademy.com") # Navigate to URl


 # -- # teram , text-info tagName
def test_core_Locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/") # Navigate to URl
    page.get_by_label("Username").fill("rahulshettyacademy") # Fill username
    page.get_by_label("password").fill("learning")  # Fill password
    page.get_by_role("combobox").select_option("teach") # Select role from dropdown
    page.get_by_role("link", name="term and conditions") #  Click on terms and conditions link
    page.locator("#terms").check() # Check the terms checkbox
    page.get_by_role("button", name="Sign in").click() # Click on Sign In button
    # This is line for assertion in worng password and username usee for learing purpose
    #expect(page.get_by_text("Incorrect username/ password.") ).to_be_visible() # Incorrect username /password -- assertion
    time.sleep(10)


 

def test_firefoxBrowser(playwright:Playwright):
    fireforBrowser=playwright.firefox.launch(headless=False)
    
    page =fireforBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/") # Navigate to URl
    page.get_by_label("Username").fill("rahulshettyacademy") # Fill username
    page.get_by_label("password").fill("learning")  # Fill password
    page.get_by_role("combobox").select_option("teach") # Select role from dropdown
    page.get_by_role("link", name="term and conditions") #  Click on terms and conditions link
    page.locator("#terms").check() # Check the terms checkbox
    page.get_by_role("button", name="Sign in").click()
     
    time.sleep(10)