### Task 2
#
#### Alerts
#
#1. Launch the browser (Chrome) and navigate to https://testautomationpractice.blogspot.com/
#2. Click on all the 3 alerts and handle them
#3. Give me the text of the result

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//button[@onclick="myFunctionAlert()"]
    Sleep    2s

    Handle Alert
    Sleep    2s

    Close Browser

Confirm Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//button[@onclick="myFunctionConfirm()"]
    Sleep    2s

    Handle Alert
    Sleep    2s
    Page Should Contain    You pressed OK!

    Close Browser

Prompt Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//button[@onclick="myFunctionPrompt()"]
    Sleep    2s

#    Handle Alert
    Input Text Into Alert  ACE
    Sleep    5s
    Page Should Contain    Hello ACE! How are you today?

    Close Browser