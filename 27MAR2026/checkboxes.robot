*** Settings ***
Documentation  handling chechboxes
Library    SeleniumLibrary

*** Variables ***
@{url}  https://the-internet.herokuapp.com/  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkboxes
    [Documentation]    herokuapp checkboxes
    Open Browser    ${url}[0]  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Checkboxes"]

    Page Should Contain Checkbox    xpath=//input[@type="checkbox"][1]

    Select Checkbox  xpath=//input[@type="checkbox"][1]
    Sleep    2s
    Unselect Checkbox  xpath=//input[@type="checkbox"][2]
    Sleep    2s
    
Checkboxes in testautomationpractice
    [Documentation]    testautomationpractice checkboxes
    Open Browser    ${url}[1]  chrome
    Maximize Browser Window
    Sleep    1s

    Page Should Contain Checkbox    id=sunday
    Select Checkbox    id=sunday
    Sleep    1s
    Page Should Contain Checkbox    id=saturday
    Select Checkbox    id=saturday
    Sleep    1s

    Click Element    id=female
    Click Element    id=male
    Sleep    1s