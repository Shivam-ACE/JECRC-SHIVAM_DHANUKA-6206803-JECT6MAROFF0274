*** Settings ***
Resource  ../../resources/pages/home_page.robot
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/common_resources.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC001
    [Documentation]  Successful Login
    [Tags]  functional

    ACCOUNT
    Login    ${USER_EMAIL}    ${USER_PWD}