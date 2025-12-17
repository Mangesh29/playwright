from playwright.sync_api import Page, expect
import time

def test_UIChecks(page:Page):
   page.goto("https://rahulshettyacademy.com/AutomationPractice/")
   expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible() # Assertion for visible
   page.get_by_role("button", name="Hide").click() #Click on hide button
   expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden() # Assertion for hidden
   

   # Alert boxes
   page.on("dialong", lambda dialog :dialog.accept()) # Handling alert
   page.get_by_role("button",name="Confirm").click() # Click on confirm button
   


   #Frames Handling 

   pageFrame = page.frame_locator("#courses-iframe") # Accessing frame
   pageFrame.get_by_role("link", name="ALL Access").click()# Click on link inside frame
   expect(pageFrame.locator("body")).to_contain_text("Happy Subscribers")
    
    
    # MouseHover
   page.locator("#mousehover").hover()
   page.get_by_role("link",name="Top").click()




    # check  the price of rice is equal to 37
    # identify the price column
    # identify  rice row
    # eatract the price values
   page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
   
   for index in range(page.locator("th").count()):
       if page.locator("th").nth(index).filter(has_text="Price").count()>0: 
           priceColValue = index;
           print(f"price column values is {priceColValue} ")
           break
   riceRow = page.locator("tr").filter(has_text="Rice")  
   expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")
   



           
        