*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling single iframe
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    
    Select Frame    id=singleframe

    Input Text    xpath=//input[@type="text"]  Shivam
    Sleep    3s

    Unselect Frame
    Unselect Frame

    Close Browser

Handling nested iframe
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[@href="#Multiple"]
    Sleep    1s

    Select Frame    xpath=//div[@id="Multiple"]/iframe
    Select Frame    xpath=//iframe[@src="SingleFrame.html"]

    Input Text    xpath=//input[@type="text"]  Shivam
    Sleep    3s

    Unselect Frame
    Unselect Frame

    Close Browser