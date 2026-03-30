*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Handling windows
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Click Element    xpath=//a[text()="Click Here"]
    Sleep    1s
    
    @{windows}=  Get Window Handles  
    @{titles}=  Get Window Titles    
    Log To Console    ${titles}[1]
    
    Switch Window    NEW

    Page Should Contain    New Window
    Page Should Contain Element    xpath=//h3[text()="New Window"]
    
    Switch Window    ${windows}[0]
    Sleep    2s
    Close Browser

