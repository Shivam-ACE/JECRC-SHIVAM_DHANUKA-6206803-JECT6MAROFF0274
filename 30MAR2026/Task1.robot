### Task 1
#
#### Window handling
#
#1. Launch the browser (Chrome) and navigate to https://testautomationpractice.blogspot.com/
#2. click on pop windows
#3. Fetch me the titles of the windows opened

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling windows
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Click Element    id=PopUp
    Sleep    1s

    @{windows}=  Get Window Handles
    @{titles}=  Get Window Titles
    Log To Console    ${titles}

    Switch Window    NEW
#    Page Should Contain Element    id=Layer_1
    
    Switch Window    ${windows}[0]
    Page Should Contain    Automation Testing Practice
    Sleep    1s

    Close Browser

