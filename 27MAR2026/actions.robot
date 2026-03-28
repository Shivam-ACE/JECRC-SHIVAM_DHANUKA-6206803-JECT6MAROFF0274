*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling Drag and Drop
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Drag and Drop"]
    Sleep    1s

    Drag And Drop    id=column-a  id=column-b
    Sleep    2s
    Close Browser

Handling Hovers
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Hovers"]
    Sleep    1s

    Mouse Over    xpath=//h5[text()="name: user2"]/ancestor::div[@class="figure"]
    Sleep    2s
    Close Browser
    
Scroll to the element
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Scroll Element Into View  xpath=//a[text()="Typos"]
    Sleep    4s
    Close Browser