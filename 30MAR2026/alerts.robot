*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//button[@onclick="jsAlert()"]
    Sleep    2s
    
    Handle Alert
    Sleep    2s

    Close Browser

Confirm Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//button[@onclick="jsConfirm()"]
    Sleep    2s

    Handle Alert  action=DISMISS
    Sleep    2s

    Close Browser

Prompt Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//button[@onclick="jsPrompt()"]
    Sleep    2s

#    Handle Alert  action=DISMISS
    Input Text Into Alert  ...............
    Sleep    2s

    Close Browser