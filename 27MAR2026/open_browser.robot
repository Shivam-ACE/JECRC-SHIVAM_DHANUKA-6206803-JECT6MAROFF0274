*** Settings ***

Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***

${url}  https://www.cricbuzz.com/   ###scalar variables
@{bikes}  ktm  kwasaki  honda  pulsar   ###List variables
&{cars}  nissan=gtr  honda=civic,verna  bmw=m5   #### dict variables

*** Test Cases ***

Opening Chrome Browser
    [Documentation]  Chrome browser navigation to https://www.cricbuzz.com/
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  ${bikes}[1]
    Log To Console  ${cars.honda}
    Sleep  3s

    Close Browser

Opening Chrome Headless Browser
    [Documentation]  Chrome browser navigation to https://www.cricbuzz.com/
#    [Tags]  smoke  reg
    Open Browser  https://www.cricbuzz.com/  headlesschrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    naviagted to cricbuzz
    Sleep    3s

    Close Browser

Open cricbuzz in edge
    Open Edge Browser

Opening FireFox Browser
    [Documentation]  Chrome browser navigation to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  firefox
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    naviagted to cricbuzz
    Sleep    3s

    Close Browser
    
*** Keywords ***

Open Edge Browser
    [Documentation]  Chrome browser navigation to https://www.cricbuzz.com/
    [Tags]    smoke reg
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    naviagted to cricbuzz
    Sleep    3s

    Close Browser