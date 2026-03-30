### Task 3
#
#### Amazon E2E
#
#1. Navigate to amazon
#2. Click on `electronics` in tab
#3. Click on `boat` checkbox
#4. Click on any product before clicking store the name of product
#5. Switch to new window
#6. Assert the product name is present in the new window
#7. Print the actual price, discounted price and the percentage
#8. Scroll to add to cart and click on the button
#9. Click on cart icon on top right corner
#10. Check if same product has been added to cart

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[@href="/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics"]
    Sleep    2s

    Click Element    xpath=//input[@id="apb-browse-refinements-checkbox_6"]/parent::label/parent::div
    Sleep    3s
    
    ${prod_name}=  Get Text    //div[@data-component-id="24"]//h2/span
    Click Element    xpath=//div[@data-component-id="24"]//img
    Sleep    2s

    Switch Window    NEW
    
    Page Should Contain    ${prod_name}
    
#    ${prices}=  Get Text    xpath=//div[@id="corePriceDisplay_desktop_feature_div"]
    
    ${actual_price}=  Get Text    xpath=(//div[@id="corePriceDisplay_desktop_feature_div"]//span[@aria-hidden="true"])[4]
    ${discounted_price}=  Get Text   xpath=(//div[@id="corePriceDisplay_desktop_feature_div"]//span[@aria-hidden="true"])[2]
    ${percent}=  Get Text    xpath=(//div[@id="corePriceDisplay_desktop_feature_div"]//span[@aria-hidden="true"])[1]

    Log To Console    Actual Price: ${actual_price}
    Log To Console    Discounted Price: ${discounted_price}
    Log To Console    Percentage: ${percent}
#    Log To Console    ${prices}

    Scroll Element Into View    id=add-to-cart-button
    Sleep    1s
    Click Element    id=add-to-cart-button
    Sleep    1s
    Click Element    id=nav-cart
    Sleep    1s
    
    Page Should Contain    ${prod_name}
    
    Close Browser