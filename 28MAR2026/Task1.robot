*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
handle multi_dropdown
    Open Browser    ${url}  ${browser}
    Maximize Browser Window

    Page Should Contain List    id=colors

    Scroll Element Into View   id=colors
    
    Sleep    1s
    
    @{options}=  Get List Items   id=colors
    Log To Console    ${options}

    Select From List By Value   id=colors  blue
    Select From List By Value   id=colors  yellow

    @{selected_options}=  Get Selected List Values      id=colors
    Log To Console    ${selected_options}

    Sleep    3s

    Close Browser