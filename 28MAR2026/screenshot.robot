*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/screenshots
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    10s

    Capture Page Screenshot    site.png
    Sleep    2s

    Scroll Element Into View    xpath=//div[text()="Dhurandhar The Revenge"]

    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  pic.png
    Sleep    2s

    Close Browser