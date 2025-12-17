from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    # iphone x, Nokia Edge -> verify 2 items are showing in cart

    page.goto("https://rahulshettyacademy.com/loginpagePractise/") # Navigate to URl
    page.get_by_label("Username").fill("rahulshettyacademy") # Fill username
    page.get_by_label("password").fill("learning")  # Fill password
    page.get_by_role("combobox").select_option("teach") # Select role from dropdown
    page.get_by_role("link", name="term and conditions") #  Click on terms and conditions link
    page.locator("#terms").check() # Check the terms checkbox
    page.get_by_role("button", name="Sign in").click()
    iphoneProduct=page.locator("app-card").filter(has_text="iphone X")  # filter with text 
    iphoneProduct.get_by_role("button").click() # Click on add to cart button
    nokiaProduct=page.locator("app-card").filter(has_text="Nokia Edge")  # filter with text 
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click() # Click on checkout button
   
    expect(page.locator(".media-body")).to_have_count(2) # Assertion for 2 items in cart 



def test_childWindowhandle(page:Page):
     # child windows handling
    page.goto("https://rahulshettyacademy.com/loginpagePractise/") #
      
      

    with page.expect_popup() as newPage_info:  #
       #step1
      #step2
            page.locator(".blinkingText").click() # Click on link which opens new page /windows 
            childPage = newPage_info.value
            text = childPage.locator(".red").text_content() # get the text from child window
            print(text)
            # Please eamil us at mentor@rahulshettyacademy.com with below template to receive to response within 24 hours.
            words = text.split("at") # 0 -> Please email us , 1 ->  mantor@rahulshettyacademy.com with below template to receive to response within 24 hours.
            email = words[1].strip().split(" ")[0]
              # ->mantor@rahulshettyacademy.com 1->
            assert email == "mentor@rahulshettyacademy.com"