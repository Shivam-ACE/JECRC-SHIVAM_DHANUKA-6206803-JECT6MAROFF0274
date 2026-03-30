*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_downloaded}  C:\\Users\\shiva\\Downloads\\file.txt

*** Test Cases ***
Upload
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s

    ${path}=  Normalize Path    I:/WEB-TECH CAP/HTML/assets/4.jpg
    Choose File    id=file-upload  ${path}
    Sleep    2s
    
    Click Element    id=file-submit

    Close Browser
    
Download
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/download"]
    Sleep    2s

    Click Element    xpath=//a[@href="download/file.txt"]
    
    Wait Until Created    ${check_downloaded}  timeout=10s
    
    File Should Exist    ${check_downloaded}
    Log To Console    it downloaded successfully
    Close Browser